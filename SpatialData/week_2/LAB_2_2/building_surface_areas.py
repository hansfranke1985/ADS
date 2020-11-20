# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:42:07 2020

@author: hansf
"""
#2.2 Obtaining building properties

from osgeo import gdal, ogr

filename = 'Amsterdam_BAG.gpkg'

data_source = ogr.GetDriverByName('GPKG').Open(filename, update=0)

#number of layers
num_layers = data_source.GetLayerCount()
print(num_layers)

#Load layer
layer_original = data_source.GetLayerByName("Pand")

#check
print("Layer:", layer_original.GetName())

from osgeo.osr import SpatialReference
rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

#Create the new dataset with the output layer centroids using a point geometry type as:
centroid_source = ogr.GetDriverByName('GPKG').CreateDataSource('centroids.gpkg')

#HERE   
centroid_layer = centroid_source.CreateLayer('centroids', srs=rdNew, geom_type=ogr.wkbPoint)


#To add a new field holding floating point values to a layer use:
field = ogr.FieldDefn("area", ogr.OFTReal)
centroid_layer.CreateField(field)

#loading definitions 
centroid_layer_def = centroid_layer.GetLayerDefn()
print(centroid_layer_def)

#You can then iterate over each feature in a layer using a for loop. For each feature retrieve the geometry with
num_features = layer_original.GetFeatureCount()
print(num_features)
for i in range(1,num_features+1):
 
    #load geometry from the original layer
    feature = layer_original.GetFeature(i)
    house_geometry = feature.GetGeometryRef()
    
    point_feature = ogr.Feature(centroid_layer_def) # get the definition for the new feature 
    point = ogr.Geometry(ogr.wkbPoint)
    
    centroid = house_geometry.Centroid() # The centroid that we want to add
    point.AddPoint(centroid.GetX(), centroid.GetY()) #  make a point from this feature
    point_feature.SetGeometry(point) # add the place of the centroid to the new point
    
    house_area = house_geometry.GetArea()
    
    point_feature.SetField('area', house_area)
    centroid_layer.CreateFeature(point_feature)
    
    
 


    
    