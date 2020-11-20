# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:05:11 2020

@author: hansf
"""

from osgeo import gdal, ogr
from osgeo.osr import SpatialReference
from tqdm import tqdm


ams_source = ogr.GetDriverByName('GPKG').Open("Amsterdam_BAG.gpkg", update=0)
district_layer = ams_source.GetLayerByName('Wijken')

centroid_source = ogr.GetDriverByName('GPKG').Open("centroids.gpkg", update=1) #update 1 is needed for adding a layer
centroid_layer = centroid_source.GetLayerByName('centroids')

if centroid_source.GetLayerByName("density"): #in case you run this script more than once
    centroid_source.DeleteLayer("density")

rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)
density_layer = centroid_source.CreateLayer('density', srs=rdNew, geom_type=ogr.wkbPoint) #create the density layer

field = ogr.FieldDefn("name", ogr.OFTString) #create fields in the layer schema
density_layer.CreateField(field)
field2 = ogr.FieldDefn("density", ogr.OFTReal) 
density_layer.CreateField(field2)
field3 = ogr.FieldDefn("fraction", ogr.OFTReal) 
density_layer.CreateField(field3)

density_layer_def = density_layer.GetLayerDefn()


for x in tqdm(range(1, district_layer.GetFeatureCount()+1)):  #for each feature in "wijken" (districts)
    district_feature = district_layer.GetFeature(x)
    district_geometry = district_feature.GetGeometryRef()
    centroid = district_geometry.Centroid()
    district_area = district_geometry.GetArea()
    name = district_feature["Buurtcombinatie"] #get the district name
    
    houses = 0
    area = 0
    
    centroid_layer.ResetReading() #don't know if I placed this right or not
    
    for y in range(1, centroid_layer.GetFeatureCount()+1):      

        centroid_feature = centroid_layer.GetFeature(y)
        centroid_geometry = centroid_feature.GetGeometryRef()
        
        if centroid_geometry.Within(district_geometry):
            houses += 1
            area += centroid_feature.area
            
    density = houses / (district_area / 1000000) # not sure, but I believe that district area is in m^2 
    fraction = area / district_area * 100
    
    point_feature = ogr.Feature(density_layer_def) # create a new feature (using the centroid_layer definition)
    point = ogr.Geometry(ogr.wkbPoint) # create a point geometry
    point.AddPoint(centroid.GetX(), centroid.GetY()) # set the coordinates of this point
    point_feature.SetGeometry(point)  
    point_feature.SetField('name', name) 
    point_feature.SetField('density', density)
    point_feature.SetField('fraction', fraction)
    
    density_layer.CreateFeature(point_feature)
    
# Question: What is the density of the district with feature id 54 (Museumkwartier)?

centroid_feature = centroid_layer.GetFeature(54)
centroid_geometry = centroid_feature.GetGeometryRef()
print(centroid_geometry)
field_value = centroid_feature.GetField("id")
print(field_value)
print("X", centroid_geometry.GetX())
print("Y", centroid_geometry.GetY())
    