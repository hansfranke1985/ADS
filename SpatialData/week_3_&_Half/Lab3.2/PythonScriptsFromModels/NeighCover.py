"""
Model exported as python.
Name : NeighCover
Group : 
With QGIS : 31415
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterField
from qgis.core import QgsProcessingParameterFeatureSource
from qgis.core import QgsProcessingParameterFeatureSink
from qgis.core import QgsCoordinateReferenceSystem
import processing


class Neighcover(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterField('Attributes', 'Attributes', type=QgsProcessingParameterField.Any, parentLayerParameterName='Landuse2017', allowMultiple=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSource('Landuse2017', 'Landuse2017', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Parkdensity', 'ParkDensity', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(7, model_feedback)
        results = {}
        outputs = {}

        # Select by attribute
        alg_params = {
            'FIELD': parameters['Attributes'],
            'INPUT': 'GRONDGEBRUIK_2017_e7cb5a9e_86ff_4002_88be_f20daea27edc',
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

        # Reproject layer
        alg_params = {
            'INPUT': outputs['ExtractSelectedFeatures']['OUTPUT'],
            'OPERATION': '',
            'OUTPUT': 'C:/UU/3-Courses/Applied data science 2020/QGIS/Lab 3.2 solution/parks_RD New.shp',
            'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:28992'),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ReprojectLayer'] = processing.run('native:reprojectlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Rasterize (vector to raster)
        alg_params = {
            'BURN': None,
            'DATA_TYPE': 5,
            'EXTENT': '110189.376500000,134030.340100000,476769.505500000,493892.184600000 [EPSG:28992]',
            'EXTRA': '',
            'FIELD': 'CBScode2',
            'HEIGHT': 40,
            'INIT': None,
            'INPUT': outputs['ReprojectLayer']['OUTPUT'],
            'INVERT': False,
            'NODATA': 0,
            'OPTIONS': '',
            'OUTPUT': 'C:/UU/3-Courses/Applied data science 2020/QGIS/Lab 3.2 solution/parksNeiRaster.tif',
            'UNITS': 1,
            'WIDTH': 40,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RasterizeVectorToRaster'] = processing.run('gdal:rasterize', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
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
            'method': 6,
            'output': 'C:/UU/3-Courses/Applied data science 2020/QGIS/Lab 3.2 solution/neighParks.tif',
            'quantile': '',
            'selection': None,
            'size': 25,
            'weight': '',
            'output': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Rneighbors'] = processing.run('grass7:r.neighbors', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Zonal statistics
        alg_params = {
            'COLUMN_PREFIX': 'PDen_',
            'INPUT_RASTER': outputs['Rneighbors']['output'],
            'INPUT_VECTOR': 'C:/UU/3-Courses/Applied data science 2020/QGIS/dataamsterdam/PC4.shp',
            'RASTER_BAND': 1,
            'STATISTICS': [2]
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatistics', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'ParkDen',
            'FIELD_PRECISION': 3,
            'FIELD_TYPE': 0,
            'FORMULA': ' \"PDen_mean\" / 40',
            'INPUT': outputs['ZonalStatistics']['INPUT_VECTOR'],
            'NEW_FIELD': True,
            'OUTPUT': parameters['Parkdensity']
        }
        outputs['FieldCalculator'] = processing.run('qgis:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Parkdensity'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'NeighCover'

    def displayName(self):
        return 'NeighCover'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Neighcover()
