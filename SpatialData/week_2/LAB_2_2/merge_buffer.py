# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:33:14 2020

@author: hansf
"""

import json
from osgeo.osr import SpatialReference, CoordinateTransformation
from osgeo import ogr, gdal

#Assign the CRS to Amsterdam
rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

data_source = ogr.GetDriverByName('GPKG').Open('schools.gpkg', update=1)

buffer_layer = data_source.GetLayerByName('buffer')

#create a new layer buffer to store new features
if data_source.GetLayerByName("merge"):
    data_source.DeleteLayer("merge")
merge_layer = data_source.CreateLayer('merge', srs=rdNew, geom_type=ogr.wkbPolygon)

#Afterwards create a new feature merge_feature and add the geometry of the first buffer feature to the new feature.
#Also add a geometry merge_geometry and initialise it with the geometry of your first feature. You will use this
#geometry to construct the merged buffer area.

buffer_feature = buffer_layer.GetNextFeature()
merge_feature = buffer_feature.GetGeometryRef()
merge_geometry = buffer_feature.GetGeometryRef()
merge_layer_def = merge_layer.GetLayerDefn()

#create new feature
    feature = ogr.Feature(buffer_layer_def)
    #set new feature's geometry
    feature.SetGeometry(buffer_geometry)
    #add new feature to the layer
    buffer_layer.CreateFeature(feature)

#ireate over buffer features:
   
    #merge the current buffer geo with previosly merged area
    union = merge_geometry.Union(buffer_geometry)
    
    #create a feature with union
    
    merge_feature = ogr.Feature(merge_layer_def)
    #update the merge geometry
    merge_geometry = merge_geometry+merge_feature
    
    merge_layer.CreateFeature(merge_geometry)