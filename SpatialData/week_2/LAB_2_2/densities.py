# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:09:10 2020

@author: hansf
"""
from osgeo import gdal, ogr
from tqdm import tqdm #progress bar

filename = 'Amsterdam_BAG.gpkg'
filename2 = 'centroids.gpkg'

#Load Sources
data_source = ogr.GetDriverByName('GPKG').Open(filename, update=0)
data_source2 = ogr.GetDriverByName('GPKG').Open(filename2, update=1)

#Load layers
layer_wijken = data_source.GetLayerByName("Wijken") #Wijken = Neighbordhoods
layer_centroids = data_source2.GetLayerByName("centroids") 
density =  data_source2.GetLayerByName("density") 

from osgeo.osr import SpatialReference
rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

#create a new layer
if data_source2.GetLayerByName("density"):
    data_source2.DeleteLayer("density")
density_layer = data_source2.CreateLayer('density', srs=rdNew, geom_type=ogr.wkbPoint)

#Add three fields to the new layer, name of type ogr.OFTString and density and fraction of type ogr.OFTReal
field = ogr.FieldDefn("name", ogr.OFTString)
density_layer.CreateField(field)

field = ogr.FieldDefn("density", ogr.OFTReal)
density_layer.CreateField(field)

field = ogr.FieldDefn("fraction", ogr.OFTReal)
density_layer.CreateField(field)


#Look for the names ofs fields
locations_def = layer_wijken.GetLayerDefn()
num_fields = locations_def.GetFieldCount()
print("Task4: Number of fields ",num_fields)

#task 4: print the name and type of each field in the layer
for i in range(0,num_fields):
    print("Name of field:",locations_def.GetFieldDefn(i).GetName())
    print("Type of field", locations_def.GetFieldDefn(i).GetTypeName())
    
#Buurtcombinatie = districts?

#3. Iterate over the districts. For each district
#a. Get the name and the size of the area of the current district, and initialise variables to store the
#number and areas of houses
layer_def = layer_wijken.GetLayerDefn()
num_fields = layer_def.GetFieldCount()
num_features = layer_wijken.GetFeatureCount()

for i in range(1,num_features+1):    
    feature = layer_wijken.GetFeature(i)
    name = feature.GetField('Buurtcombinatie')
    geometry = feature.GetGeometryRef()
    print(name, geometry.GetArea())

#b. Iterating over a layer works once. For a repeated iteration over a layer you need to use
#ResetReading() before you attempt to iterate another time:

#centroid_layer.ResetReading()
    
#c. c. For each centroid test whether it is in the current district geometry. If so, accumulate the number and
#area. You can use Within to test the geometries:
density_layer_def = density_layer.GetLayerDefn()
    
for x in tqdm(range(1, layer_wijken.GetFeatureCount()+1)):  #for each feature in "wijken" (districts)
    district_feature = layer_wijken.GetFeature(x)
    district_geometry = district_feature.GetGeometryRef()
    centroid = district_geometry.Centroid()
    district_area = district_geometry.GetArea()
    name = district_feature["Buurtcombinatie"] #get the district name
    
    houses = 0
    area = 0
    
    layer_centroids.ResetReading() 
    
    for y in range(1, layer_centroids.GetFeatureCount()+1):      

        centroid_feature = layer_centroids.GetFeature(y)
        centroid_geometry = centroid_feature.GetGeometryRef()
        
        if centroid_geometry.Within(district_geometry):
            houses += 1
            area += centroid_feature.area

    #d. Compute the density and fraction and assign these with the name of the current district to the output
#layer               
    density = houses / (district_area / 1000000) 
    fraction = area / district_area * 100
    
    point_feature = ogr.Feature(density_layer_def) # create a new feature 
    point = ogr.Geometry(ogr.wkbPoint) # create a point geometry
    point.AddPoint(centroid.GetX(), centroid.GetY()) # set the coordinates of this point
    point_feature.SetGeometry(point)  
    point_feature.SetField('name', name) 
    point_feature.SetField('density', density)
    point_feature.SetField('fraction', fraction)
    
    density_layer.CreateFeature(point_feature)
            
#d. Compute the density and fraction and assign these with the name of the current district to the output
#layer    

## Question: What is the density of the district with feature id 54 (Museumkwartier)?


c_db = ogr.GetDriverByName('GPKG').Open("centroids.gpkg", update=0)
density = c_db.GetLayerByName('density')
density.GetFeature(54).GetField("density")



