"""
Model exported as python.
Name : AreaInterpolation
Group : AreaInterpolation
With QGIS : 31415
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
import processing


class Areainterpolation(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('JoinLayer', 'Source Layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('TargetLayer', 'Target Layer', defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(5, model_feedback)
        results = {}
        outputs = {}

        # Intersection
        alg_params = {
            'INPUT': parameters['TargetLayer'],
            'INPUT_FIELDS': [''],
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/area_interpolation_data/clipped.shp',
            'OVERLAY': parameters['JoinLayer'],
            'OVERLAY_FIELDS': [''],
            'OVERLAY_FIELDS_PREFIX': '',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Intersection'] = processing.run('native:intersection', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Add geometry attributes
        alg_params = {
            'CALC_METHOD': 0,
            'INPUT': outputs['Intersection']['OUTPUT'],
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/area_interpolation_data/add_geom.shp',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'product',
            'FIELD_PRECISION': 3,
            'FIELD_TYPE': 0,
            'FORMULA': 'CASE \r\nWHEN attribute($currentfeature, \'BU_CODE\') IS NULL OR attribute($currentfeature, \'P_65_EO_JR\') <= 0 THEN NULL ELSE attribute($currentfeature, \'area\') * attribute($currentfeature, \'P_65_EO_JR\')\r\nEND',
            'INPUT': outputs['AddGeometryAttributes']['OUTPUT'],
            'NEW_FIELD': True,
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/area_interpolation_data/calc.shp',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('qgis:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Aggregate
        alg_params = {
            'AGGREGATES': [{'aggregate': 'first_value','delimiter': ',','input': '\"Postcode4\"','length': 4,'name': 'Postcode4','precision': 0,'type': 2},{'aggregate': 'sum','delimiter': ',','input': '\"area\"','length': 23,'name': 'area','precision': 15,'type': 6},{'aggregate': 'sum','delimiter': ',','input': '\"product\"','length': 10,'name': 'product','precision': 3,'type': 6}],
            'GROUP_BY': 'Postcode4',
            'INPUT': outputs['FieldCalculator']['OUTPUT'],
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/area_interpolation_data/aggr.shp',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Aggregate'] = processing.run('native:aggregate', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'WVALUE',
            'FIELD_PRECISION': 3,
            'FIELD_TYPE': 0,
            'FORMULA': 'attribute($currentfeature, \'product\') / attribute($currentfeature, \'area\')',
            'INPUT': outputs['Aggregate']['OUTPUT'],
            'NEW_FIELD': True,
            'OUTPUT': 'C:/UU/3_Courses/Applied data science 2020/Lab3.1/Lab3.1 solution/area_interpolation_data/final.shp',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('qgis:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'AreaInterpolation'

    def displayName(self):
        return 'AreaInterpolation'

    def group(self):
        return 'AreaInterpolation'

    def groupId(self):
        return 'AreaInterpolation'

    def createInstance(self):
        return Areainterpolation()
