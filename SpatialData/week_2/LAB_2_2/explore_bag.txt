# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:27:24 2020

@author: hansf
"""

from osgeo import gdal, ogr

filename = 'Amsterdam_BAG.gpkg'

data_source = ogr.GetDriverByName('GPKG').Open(filename, update=0)

#Task1: Print the number of Layers Included in Dataset:
print("Task1: Layers",data_source.GetLayerCount())


#number of layers
num_layers = data_source.GetLayerCount()

#Task2: Print for each layer the layer name and CRS
for i in range(0,num_layers):
    layer = data_source.GetLayerByIndex(i)
    srs = layer.GetSpatialRef()
    
    print("Layer:", i, layer.GetName())
    print("CRS", srs)
    print("\n")
    
print("End TASK \n\n\n")

buildings = data_source.GetLayerByName('Verblijfsobject')

#task3: Print the number of Features in the layer
print("Task3: Layer name", buildings.GetName())
print("Task3: Features", buildings.GetFeatureCount())


locations_def = buildings.GetLayerDefn()
num_fields = locations_def.GetFieldCount()
print("Task4: Number of fields ",num_fields)

#task 4: print the name and type of each field in the layer
for i in range(0,num_fields):
    print("Name of field:",locations_def.GetFieldDefn(i).GetName())
    print("Type of field", locations_def.GetFieldDefn(i).GetTypeName())
   

#task5: Add code to your script that iterates over all features in the layer, retrieves the value of the field oppervlakte
#(surface area) and adds up the area.
# oppervlakte = "Surface"

# Question: What is the total surface area given in the location layer?

num_features = buildings.GetFeatureCount()
print("Number of features:", num_features)

field_name = "oppervlakte"
area = 0
for i in range(1,num_features+1):
    
    feature = buildings.GetFeature(i)
    field_value = feature.GetField(field_name)
    area = area + field_value
print("Total area:", area)
    
  
#Question: What is the coordinate of the feature with the index 439774?    
feature = buildings.GetFeature(439774)
geometry = feature.GetGeometryRef()
print(geometry)
print("X", geometry.GetX())
print("Y", geometry.GetY())




