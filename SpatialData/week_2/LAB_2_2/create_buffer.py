# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:44:29 2020

@author: hansf
"""

import json
from osgeo.osr import SpatialReference, CoordinateTransformation
from osgeo import ogr, gdal

data_source = ogr.GetDriverByName('GPKG').Open('schools.gpkg', update=1) 
point_layer = data_source.GetLayerByName('locations')
# add a new layer buffer. The layer will be used to store the new features.
rdNew = SpatialReference() 
rdNew.ImportFromEPSG(28992)
#check if buffer layer exists alreadry and remove it
if data_source.GetLayerByName('buffer'):
    data_source.DeleteLayer('buffer')

    print('Layer buffer removed!!!')
#add new layer to the dataset
buffer_layer = data_source.CreateLayer('buffer', srs=rdNew, geom_type=ogr.wkbPolygon)
buffer_layer_def = buffer_layer.GetLayerDefn()
buffer_distance=250
for c in range(1,point_layer.GetFeatureCount()+1): 
    point_feature=point_layer.GetFeature(c)
    point_geometry = point_feature.GetGeometryRef() 
    buffer_geometry = point_geometry.Buffer(buffer_distance)
    #create new feature
    feature = ogr.Feature(buffer_layer_def)
    #set new feature's geometry
    feature.SetGeometry(buffer_geometry)
    #add new feature to the layer
    buffer_layer.CreateFeature(feature)