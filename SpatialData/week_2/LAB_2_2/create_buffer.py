# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:44:29 2020

@author: hansf
"""

import json
from osgeo.osr import SpatialReference, CoordinateTransformation
from osgeo import ogr, gdal

#Assign the CRS to Amsterdam
rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

data_source = ogr.GetDriverByName('GPKG').Open('schools.gpkg', update=1)

point_layer = data_source.GetLayerByName('locations')

#create a new layer buffer to store new features
if data_source.GetLayerByName("buffer"):
    data_source.DeleteLayer("buffer")
buffer_layer = data_source.CreateLayer('buffer', srs=rdNew, geom_type=ogr.wkbPolygon)


#Iterate over all features in the point layer and retrieve each point geometry. You can then use the Buffer method to
#add a buffer around the point:

#create 250m as exercise suggestion    
buffer_distance = 250

point_layer_def = point_layer.GetLayerDefn()
num_features = point_layer.GetFeatureCount() #set limit of iterations

#iterate all over the features in the points and add a buff around the point   
for i in range(1,num_features+1):
    point_feature = point_layer.GetFeature(i)    
    point_geometry = point_feature.GetGeometryRef()
    buffer_geometry = point_geometry.Buffer(buffer_distance) #add the distance set in each point
#    print(point_geometry)
#    print(buffer_geometry)
    buffer_layer_def = buffer_layer.GetLayerDefn()
    #create new feature
    feature = ogr.Feature(buffer_layer_def)
    #set new feature's geometry
    feature.SetGeometry(buffer_geometry)
    #add new feature to the layer
    buffer_layer.CreateFeature(feature)
    