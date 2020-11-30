"""
Model exported as python.
Name : NeighCover
Group : Lab3.2
With QGIS : 31600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterField
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Neighcover(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterField('Attributes', '“Attributes”', type=QgsProcessingParameterField.String, parentLayerParameterName='Landuse2017', allowMultiple=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterVectorLayer('Landuse2017', 'Landuse2017', defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Parkdensity', 'ParkDensity', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(6, model_feedback)
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

        # r.neighbors
        alg_params = {
            '-a': False,
            '-c': False,
            'GRASS_RASTER_FORMAT_META': '',
            'GRASS_RASTER_FORMAT_OPT': '',
            'GRASS_REGION_CELLSIZE_PARAMETER': 0,
            'GRASS_REGION_PARAMETER': None,
            'gauss': None,
            'input': outputs['RasterizeVectorToRaster']['OUTPUT'],
            'method': 7,
            'output': 'C:/Users/hansf/Documents/GitHub/ADS/SpatialData/week_3_&_Half/Lab3.2/Lab3.2 solution/neighParks.tif',
            'quantile': '',
            'selection': None,
            'size': 25,
            'weight': '',
            'output': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Rneighbors'] = processing.run('grass7:r.neighbors', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Zonal statistics
        alg_params = {
            'COLUMN_PREFIX': 'PDean_',
            'INPUT_RASTER': outputs['Rneighbors']['output'],
            'INPUT_VECTOR': 'PC4_4dd719c3_eede_4894_b303_e3a7b00e5301',
            'RASTER_BAND': 1,
            'STATISTICS': [2]
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatistics', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'ParkDen',
            'FIELD_PRECISION': 2,
            'FIELD_TYPE': 0,
            'FORMULA': '\"PDean_me_1\" / 40',
            'INPUT': outputs['ZonalStatistics']['INPUT_VECTOR'],
            'OUTPUT': parameters['Parkdensity']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Parkdensity'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'NeighCover'

    def displayName(self):
        return 'NeighCover'

    def group(self):
        return 'Lab3.2'

    def groupId(self):
        return 'Lab3.2'

    def createInstance(self):
        return Neighcover()
