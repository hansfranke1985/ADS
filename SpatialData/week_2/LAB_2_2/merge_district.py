import json
from osgeo.osr import SpatialReference, CoordinateTransformation
from osgeo import ogr, gdal

#Assign the CRS to Amsterdam
rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

data_source = ogr.GetDriverByName('GPKG').Open('schools.gpkg', update=1)

wijken_data_source = ogr.GetDriverByName('GPKG').Open("Amsterdam_BAG.gpkg", update=1)
wijken_layer = wijken_data_source.GetLayerByName('Wijken')

rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

if data_source.GetLayerByName("districts"):
    data_source.DeleteLayer("districts")
districts_layer = data_source.CreateLayer('districts', srs=rdNew, geom_type=ogr.wkbMultiPolygon)
districts_feature_def = districts.GetLayerDefn() # define new layer

wijken_feature = wijken_layer.GetNextFeature() # get first feature of buffer
wijken_geometry = wijken_feature.GetGeometryRef()

districts_feature = ogr.Feature(districts_feature_def) # initialize the merge_feature
districts_feature.SetGeometry(wijken_geometry)
districts_geometry = districts_feature.GetGeometryRef() # set the merge_geometry

for i in range(1,len(wijken_layer)):
    wijken_feature = wijken_layer.GetNextFeature()
    wijken_geometry = wijken_feature.GetGeometryRef()
    
    union = districts_geometry.Union(wijken_geometry)
    districts_feature.SetGeometry(union)
    districts_geometry = districts_feature.GetGeometryRef() 
    
# Save the new feature to the the districs layer
districts_layer.CreateFeature(districts_feature)

#school_away code
merge_layer = data_source.GetLayerByName('merge')
merge_layer_def = merge_layer.GetLayerDefn()


# and add a new layer away 
if data_source.GetLayerByName('away'):
    data_source.DeleteLayer("away")
away = data_source.CreateLayer('away', srs=rdNew, geom_type=ogr.wkbMultiPolygon)
away_feature_def = away.GetLayerDefn() # define new layer
away_feature = ogr.Feature(away_feature_def)

districts_layer.SymDifference(merge_layer, away)
feature_away = away.GetFeature(1)
gem_away = feature_away.GetGeometryRef()
print('The area considered far away from schools is (m2): ', gem_away.GetArea())