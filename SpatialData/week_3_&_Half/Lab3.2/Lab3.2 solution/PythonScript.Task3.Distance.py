"""
Model exported as python.
Name : DistanceA
Group : Lab3.2
With QGIS : 31600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterField
from qgis.core import QgsProcessingParameterVectorLayer
import processing


class Distancea(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterField('Attributes', '“Attributes”', type=QgsProcessingParameterField.String, parentLayerParameterName='Landuse2017', allowMultiple=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterVectorLayer('Landuse2017', 'Landuse2017', defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(5, model_feedback)
        results = {}
        outputs = {}

        # Select by attribute
        alg_params = {
            'FIELD': parameters['Attributes'],
            'INPUT': parameters['Landuse2017'],
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
            'OUTPUT': 'C:/Users/hansf/Documents/GitHub/ADS/SpatialData/week_3_&_Half/Lab3.2/Lab3.2 solution/parks.shp',
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
            'EXTENT': '110127.118600000,133575.924500000,476420.651300000,494400.149500000 [EPSG:28992]',
            'EXTRA': '',
            'FIELD': 'CBScode2',
            'HEIGHT': 40,
            'INIT': None,
            'INPUT': outputs['ExtractSelectedFeatures']['OUTPUT'],
            'INVERT': False,
            'NODATA': 0,
            'OPTIONS': '',
            'OUTPUT': 'C:/Users/hansf/Documents/GitHub/ADS/SpatialData/week_3_&_Half/Lab3.2/Lab3.2 solution/parksRaster.tif',
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
            'OUTPUT': 'C:/Users/hansf/Documents/GitHub/ADS/SpatialData/week_3_&_Half/Lab3.2/Lab3.2 solution/dist2parks.tif',
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
            'INPUT_VECTOR': 'PC4_5e025dc1_4a68_46ae_a1fd_4cabb1f71d94',
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
        return 'Lab3.2'

    def groupId(self):
        return 'Lab3.2'

    def createInstance(self):
        return Distancea()
