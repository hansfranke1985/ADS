"""
Model exported as python.
Name : AreaInterpolation
Group : AreaInterpolation
With QGIS : 31600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Areainterpolation(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('TargetLayer', 'Target Layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('SourceLayer', 'Source Layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Aggr', 'aggr', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Calc', 'calc', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Final', 'final', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Clipped', 'clipped', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Add_geom', 'add_geom', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

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
            'OVERLAY': parameters['SourceLayer'],
            'OVERLAY_FIELDS': [''],
            'OVERLAY_FIELDS_PREFIX': '',
            'OUTPUT': parameters['Clipped']
        }
        outputs['Intersection'] = processing.run('native:intersection', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Clipped'] = outputs['Intersection']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Add geometry attributes
        alg_params = {
            'CALC_METHOD': 0,
            'INPUT': outputs['Intersection']['OUTPUT'],
            'OUTPUT': parameters['Add_geom']
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Add_geom'] = outputs['AddGeometryAttributes']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'final',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,
            'FORMULA': 'attribute($currentfeature, \'product\') / attribute($currentfeature, \'area\')',
            'INPUT': 'Aggregated_617e3b9b_1ec2_431d_8679_90f51a214e8c',
            'OUTPUT': parameters['Final']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Final'] = outputs['FieldCalculator']['OUTPUT']

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'product',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,
            'FORMULA': 'CASE\r\nWHEN attribute($currentfeature, \'BU_CODE\') IS NULL\r\nOR attribute($currentfeature, \'P_65_EO_JR\') <= 0\r\nTHEN NULL\r\nELSE attribute($currentfeature, \'area\') * attribute($currentfeature,\r\n\'P_65_EO_JR\')\r\nEND\r\n',
            'INPUT': outputs['AddGeometryAttributes']['OUTPUT'],
            'OUTPUT': parameters['Calc']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Calc'] = outputs['FieldCalculator']['OUTPUT']

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Aggregate
        alg_params = {
            'AGGREGATES': [{'aggregate': 'first_value','delimiter': ',','input': '\"Postcode4\"','length': 4,'name': 'Postcode4','precision': 0,'type': 2},{'aggregate': 'sum','delimiter': ',','input': '\"area\"','length': 23,'name': 'area','precision': 15,'type': 6},{'aggregate': 'sum','delimiter': ',','input': '\"product\"','length': 23,'name': 'product','precision': 15,'type': 6}],
            'GROUP_BY': 'Postcode4',
            'INPUT': outputs['FieldCalculator']['OUTPUT'],
            'OUTPUT': parameters['Aggr']
        }
        outputs['Aggregate'] = processing.run('native:aggregate', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Aggr'] = outputs['Aggregate']['OUTPUT']
        return results

    def name(self):
        return 'AreaInterpolation'

    def displayName(self):
        return 'AreaInterpolation'

    def group(self):
        return 'AreaInterpolation'

    def groupId(self):
        return ''

    def createInstance(self):
        return Areainterpolation()
