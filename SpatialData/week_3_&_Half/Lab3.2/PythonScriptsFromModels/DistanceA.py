"""
Model exported as python.
Name : DistanceA
Group : DistanceA
With QGIS : 31415
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterField
from qgis.core import QgsProcessingParameterVectorLayer
import processing


class Distancea(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterField('Attributes', 'Attributes', type=QgsProcessingParameterField.Any, parentLayerParameterName='Landuse20171', allowMultiple=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterVectorLayer('Landuse20171', 'Landuse2017', defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(5, model_feedback)
        results = {}
        outputs = {}

        # Select by attribute
        alg_params = {
            'FIELD': parameters['Attributes'],
            'INPUT': parameters['Landuse20171'],
            'METHOD': 0,
            'OPERATOR': 0,
            'VALUE': '40'
        }
        outputs['SelectByAttribute'] = processing.run('qgis:selectbyattribute', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Extract selected features
        alg_params = {
            'INPUT': outputs['SelectByAttribute']['OUTPUT'],
            'OUTPUT': 'C:/UU/3-Courses/Applied data science 2020/QGIS/Lab 3.2 solution/parks.shp',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractSelectedFeatures'] = processing.run('native:saveselectedfeatures', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Rasterize (vector to raster)
        alg_params = {
            'BURN': 0,
            'DATA_TYPE': 5,
            'EXTENT': '110189.376500000,134030.340100000,476769.505500000,493892.184600000 [EPSG:28992]',
            'EXTRA': '',
            'FIELD': 'CBScode2',
            'HEIGHT': 40,
            'INIT': None,
            'INPUT': outputs['ExtractSelectedFeatures']['OUTPUT'],
            'INVERT': False,
            'NODATA': 0,
            'OPTIONS': '',
            'OUTPUT': 'C:/UU/3-Courses/Applied data science 2020/Lab 3.2 solution/parksRaster.tif',
            'UNITS': 1,
            'WIDTH': 40,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RasterizeVectorToRaster'] = processing.run('gdal:rasterize', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Proximity (raster distance)
        alg_params = {
            'BAND': 1,
            'DATA_TYPE': 5,
            'EXTRA': '',
            'INPUT': outputs['RasterizeVectorToRaster']['OUTPUT'],
            'MAX_DISTANCE': 0,
            'NODATA': 0,
            'OPTIONS': '',
            'OUTPUT': 'C:/UU/3-Courses/Applied data science 2020/Lab 3.2 solution/dist2parks.tif',
            'REPLACE': 0,
            'UNITS': 0,
            'VALUES': '',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ProximityRasterDistance'] = processing.run('gdal:proximity', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Zonal statistics
        alg_params = {
            'COLUMN_PREFIX': 'dist_',
            'INPUT_RASTER': outputs['ProximityRasterDistance']['OUTPUT'],
            'INPUT_VECTOR': 'PC4_77036593_f2a1_4430_8bb8_b43d6b88a523',
            'RASTER_BAND': 1,
            'STATISTICS': [2]
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatistics', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'DistanceA'

    def displayName(self):
        return 'DistanceA'

    def group(self):
        return 'DistanceA'

    def groupId(self):
        return 'DistanceA_1'

    def createInstance(self):
        return Distancea()
