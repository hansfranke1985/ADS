# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:54:47 2020

@author: hansf
"""

from osgeo import gdal, ogr
from osgeo.osr import SpatialReference
from tqdm import tqdm

# 2.3
rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

a_db = ogr.GetDriverByName('GPKG').Open("Amsterdam_BAG.gpkg", update=0)
wijken = a_db.GetLayerByName('Wijken')

cent_db = ogr.GetDriverByName('GPKG').Open("centroids.gpkg", update=1)
cent_layer = cent_db.GetLayerByName('centroids')

# Create a new output layer density in the dataset centroids.gkpg
density_layer = cent_db.CreateLayer('density2', srs=rdNew, geom_type=ogr.wkbPoint)

# Add three fields to the new layer, name of type ogr.OFTString and density and fraction of type ogr.OFTReal
name_field = ogr.FieldDefn('name', ogr.OFTString)
density_field = ogr.FieldDefn('density', ogr.OFTReal)
fraction_field = ogr.FieldDefn('fraction', ogr.OFTReal)

density_layer.CreateField(name_field)
density_layer.CreateField(density_field)
density_layer.CreateField(fraction_field)

# Create layer definition
density_layer_def = density_layer.GetLayerDefn()

# Iterate over the districts, for each district:
for i in tqdm(range(1, wijken.GetFeatureCount() + 1)):
    # Get the name and the size of the area of the current district, and
    # initialise variables to store the number and areas of houses
    district = wijken.GetFeature(i)

    district_name = district.GetField(0)  # get name
    district_geom = district.GetGeometryRef()  # get geom ref
    district_centroid = district_geom.Centroid()
    district_area = district_geom.GetArea()  # get area

    # Initialize variables
    total_area = 0.0
    total_houses = 0

    # Iterating over a layer works once. For a repeated iteration over a layer you need to use
    # ResetReading() before you attempt to iterate another time:
    cent_layer.ResetReading()

    for j in tqdm(range(1, cent_layer.GetFeatureCount())):
        cent_feature = cent_layer.GetFeature(j)
        cent_geom = cent_feature.GetGeometryRef()

        # For each centroid test whether it is in the current district geometry. If so, accumulate
        # the number and area. You can use Within to test the geometries:
        if cent_geom.Within(district_geom):
            total_area += cent_feature.GetField('area')
            total_houses += 1

    # Create a new feature
    point_feature = ogr.Feature(density_layer_def)
    # create a new point geometry
    point = ogr.Geometry(ogr.wkbPoint)
    # Passing X and Y coordinats of centroids of the houses to new point
    point.AddPoint(district_centroid.GetX(), district_centroid.GetY())
    point_feature.SetGeometry(point)

    # Compute the density and fraction and assign these with the name of the
    # current district to the output layer
    point_feature.SetField('name', district_name)
    point_feature.SetField('density', total_houses/district_area)
    point_feature.SetField('fraction', total_houses/total_area)
    density_layer.CreateFeature(point_feature)

# What is the density of the district with feature id 54 (Museumkwartier)?
c_db = ogr.GetDriverByName('GPKG').Open("centroids.gpkg", update=0)
density = c_db.GetLayerByName('density')
density.GetFeature(54).GetField(0)
# 0.0021170744760404285