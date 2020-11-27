"""
Model exported as python.
Name : FieldAgg
Group : FieldAgg
With QGIS : 31600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterRasterDestination
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Fieldagg(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('Postalcodeareas', 'Postal code areas', defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Landuse_raster', 'Landuse_raster', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Parkarea', 'parkarea', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Parks', 'parks', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        results = {}
        outputs = {}

        # Rasterize (vector to raster)
        alg_params = {
            'BURN': 0,
            'DATA_TYPE': 5,
            'EXTENT': '110189.376500000,134030.340100000,476769.505500000,493892.184600000 [EPSG:28992]',
            'EXTRA': '',
            'FIELD': 'CBScode2',
            'HEIGHT': 50,
            'INIT': None,
            'INPUT': 'GRONDGEBRUIK_2017_RDNew_133b875e_615b_46e4_8fa8_3d9ade9ba3f2',
            'INVERT': False,
            'NODATA': 0,
            'OPTIONS': '',
            'UNITS': 1,
            'WIDTH': 50,
            'OUTPUT': parameters['Landuse_raster']
        }
        outputs['RasterizeVectorToRaster'] = processing.run('gdal:rasterize', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Landuse_raster'] = outputs['RasterizeVectorToRaster']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Reclassify by table
        alg_params = {
            'DATA_TYPE': 5,
            'INPUT_RASTER': outputs['RasterizeVectorToRaster']['OUTPUT'],
            'NODATA_FOR_MISSING': True,
            'NO_DATA': -9999,
            'RANGE_BOUNDARIES': 0,
            'RASTER_BAND': 1,
            'TABLE': [39.5,40.5,40],
            'OUTPUT': parameters['Parks']
        }
        outputs['ReclassifyByTable'] = processing.run('native:reclassifybytable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Parks'] = outputs['ReclassifyByTable']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Zonal statistics
        alg_params = {
            'COLUMN_PREFIX': 'Park_',
            'INPUT_RASTER': outputs['ReclassifyByTable']['OUTPUT'],
            'INPUT_VECTOR': parameters['Postalcodeareas'],
            'RASTER_BAND': 1,
            'STATISTICS': [0]
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatistics', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'parkarea',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,
            'FORMULA': 'attribute($currentfeature, \'Park_cou_1\') / attribute($currentfeature, \'Opp_m2\')',
            'INPUT': outputs['ZonalStatistics']['INPUT_VECTOR'],
            'OUTPUT': parameters['Parkarea']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Parkarea'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'FieldAgg'

    def displayName(self):
        return 'FieldAgg'

    def group(self):
        return 'FieldAgg'

    def groupId(self):
        return ''

    def createInstance(self):
        return Fieldagg()
