#-------------------------------------------------------------------------------
# Name:        Aggregation functions in QGIS
# Purpose:     Implement different spatial analysis, overlay and data aggregation functions in Python using PyQGIS
#
# Author:      Simon Scheider, Haiqi
#
# Created:     8/11/2020
# With QGIS :  3.14.15
#-------------------------------------------------------------------------------

import os, sys
from qgis.core import *
from qgis.analysis import QgsNativeAlgorithms

#See https://gis.stackexchange.com/a/155852/4972 for details about the prefix
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.14/apps/qgis", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append(r'C:\Program Files\QGIS 3.14\apps\qgis\python\plugins')
import processing  # In order to call algorithms
from processing.core.Processing import Processing
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

#Set directory, CRS
amsterdamfolder = r'C:\UU\3_Courses\Applied data science 2020\dataAmsterdam'
#crs = QgsCoordinateReferenceSystem("EPSG:28992")

#Standard source data
pc4layer = QgsVectorLayer(os.path.join(amsterdamfolder,'PC4.shp') , 'PC4', 'ogr')
cbslayer = QgsVectorLayer(os.path.join(amsterdamfolder,'CBS_Buurt_2014_AP_RDNew.shp') , 'CBS', 'ogr')
resultfolder = r'C:\UU\3_Courses\Applied data science 2020\PythonEx\ArealInterp'

# Function for Task1 workflow -  Areal Interpolation
def arealInterpol(targetfile=pc4layer, overlayfile=cbslayer, outputfile='final.shp'):

    # Intersection
    alg_params = {
        'INPUT': targetfile,
        'INPUT_FIELDS': [''],
        'OUTPUT': os.path.join(resultfolder, 'clipped.shp'),
        'OVERLAY': overlayfile,
        'OVERLAY_FIELDS': [''],
        'OVERLAY_FIELDS_PREFIX': '',
    }
    clipped = processing.run('native:intersection', alg_params)

    # Add geometry attributes
    alg_params = {
        'CALC_METHOD': 0,
        'INPUT': clipped['OUTPUT'],
        'OUTPUT': os.path.join(resultfolder, 'add_geom.shp'),
    }
    add_geom = processing.run('qgis:exportaddgeometrycolumns', alg_params)

    # Field calculator
    alg_params = {
        'FIELD_LENGTH': 23,
        'FIELD_NAME': 'product',
        'FIELD_PRECISION': 3,
        'FIELD_TYPE': 0,
        'FORMULA': 'CASE \r\nWHEN attribute($currentfeature, \'BU_CODE\') IS NULL OR attribute($currentfeature, \'P_65_EO_JR\') <= 0 THEN NULL ELSE attribute($currentfeature, \'area\') * attribute($currentfeature, \'P_65_EO_JR\')\r\nEND',
        'INPUT': add_geom['OUTPUT'],
        'NEW_FIELD': True,
        'OUTPUT': os.path.join(resultfolder, 'calc.shp'),
    }
    calc = processing.run('qgis:fieldcalculator', alg_params)

    # Aggregate
    alg_params = {
        'AGGREGATES': [
            {'aggregate': 'first_value', 'delimiter': ',', 'input': '\"Postcode4\"', 'length': 4, 'name': 'Postcode4',
             'precision': 0, 'type': 2},
            {'aggregate': 'sum', 'delimiter': ',', 'input': '\"area\"', 'length': 23, 'name': 'area', 'precision': 15,
             'type': 6},
            {'aggregate': 'sum', 'delimiter': ',', 'input': '\"product\"', 'length': 23, 'name': 'product',
                          'precision': 3, 'type': 6}],
        'GROUP_BY': 'Postcode4',
        'INPUT': calc['OUTPUT'],
        'OUTPUT': os.path.join(resultfolder, 'aggr.shp'),
    }
    aggr = processing.run('native:aggregate', alg_params)

    # Field calculator
    alg_params = {
        'FIELD_LENGTH': 10,
        'FIELD_NAME': 'WVALUE',
        'FIELD_PRECISION': 3,
        'FIELD_TYPE': 0,
        'FORMULA': 'attribute($currentfeature, \'product\') / attribute($currentfeature, \'area\')',
        'INPUT': aggr['OUTPUT'],
        'NEW_FIELD': True,
        'OUTPUT': os.path.join(resultfolder, outputfile),
    }
    result = processing.run('qgis:fieldcalculator', alg_params)

    print("Interpolated " + overlayfile.name() + "'s attribute " + 'P_65_EO_JR' + " into " + targetfile.name())
    return result

def fieldAgg(targetfile =pc4layer, cbscode='40', fieldname='parkarea', outputfile='parkarea.shp'):

    """This needs to be filled by your own code"""

    print ("Aggregated "+GRONDGEBRUIK_2017+"'s class "+str(cbscode)+ " into "+ targetfile.name())
    return parkarea

#Distance analysis and aggregation
def distanceA(targetfile = pc4layer, cbscode='40', outputfile='accessparks.shp'):

    """This needs to be filled by your own code"""

    return accessibility

#Focal coverage aggregation
def focalCover(targetfile = pc4layer, cbscode='40', outputfile='coverageparks.shp'):

    """This needs to be filled by your own code"""

    return focalsum


def main():
    arealInterpol(targetfile=pc4layer, overlayfile=cbslayer, outputfile='final.shp')



if __name__ == '__main__':
    main()