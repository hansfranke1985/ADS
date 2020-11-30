"""
Model exported as python.
Name : FieldAgg
Group : FieldAgg
With QGIS : 31415
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
import processing


class Fieldagg(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('Landuse', 'Land use', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('Postalcodeareas', 'Postal code areas', defaultValue=None))

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
            'EXTENT': '110004.147200000,134427.875400000,476420.537300000,494400.256700000 [EPSG:28992]',
            'EXTRA': '',
            'FIELD': 'CBScode2',
            'HEIGHT': 50,
            'INIT': None,
            'INPUT': parameters['Landuse'],
            'INVERT': False,
            'NODATA': 0,
            'OPTIONS': '',
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/map_algebra_data/Landuse_InterRaster.tif',
            'UNITS': 1,
            'WIDTH': 50,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RasterizeVectorToRaster'] = processing.run('gdal:rasterize', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Reclassify by table
        alg_params = {
            'DATA_TYPE': 5,
            'INPUT_RASTER': outputs['RasterizeVectorToRaster']['OUTPUT'],
            'NODATA_FOR_MISSING': True,
            'NO_DATA': -9999,
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/map_algebra_data/park.tif',
            'RANGE_BOUNDARIES': 0,
            'RASTER_BAND': 1,
            'TABLE': [39.5,40.5,1],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ReclassifyByTable'] = processing.run('native:reclassifybytable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

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
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'Parkarea',
            'FIELD_PRECISION': 3,
            'FIELD_TYPE': 0,
            'FORMULA': ' (attribute($currentfeature, \'Park_count\') * 50 * 50) / attribute($currentfeature, \'Opp_m2\')',
            'INPUT': outputs['ZonalStatistics']['INPUT_VECTOR'],
            'NEW_FIELD': True,
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/map_algebra_data/parkarea1.shp',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('qgis:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'FieldAgg'

    def displayName(self):
        return 'FieldAgg'

    def group(self):
        return 'FieldAgg'

    def groupId(self):
        return 'FieldAgg'

    def createInstance(self):
        return Fieldagg()
