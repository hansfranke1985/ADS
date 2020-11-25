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
merge_layer = data_source.CreateLayer('merge', srs=rdNew, geom_type=ogr.wkbMultiPolygon)
merge_layer_def = buffer_layer.GetLayerDefn()

#Afterwards create a new feature merge_feature and add the geometry of the first buffer feature to the new feature.
#Also add a geometry merge_geometry and initialise it with the geometry of your first feature. You will use this
#geometry to construct the merged buffer area.
buffer_feature = buffer_layer.GetNextFeature()
buffer_geometry = buffer_feature.GetGeometryRef()
#create new feature
merge_feature = ogr.Feature(merge_layer_def)
#add geometry of buffer feature to new merge feature
merge_feature.SetGeometry(buffer_geometry)
merge_geometry= merge_feature.GetGeometryRef()

for c in range(1,buffer_layer.GetFeatureCount()+1):
    # Get the geometry of the current buffer feature
    buffer_feature=buffer_layer.GetFeature(c)
    buffer_geometry = buffer_feature.GetGeometryRef()
    # Merge the current buffer geometry with the previously merged area
    union = merge_geometry.Union(buffer_geometry)
    # Create a feature with the merged geometry
    merge_feature = ogr.Feature(merge_layer_def)
    merge_feature.SetGeometry(union)
    # update merge_geometry
    merge_geometry= merge_feature.GetGeometryRef()
#create new feature
feature = ogr.Feature(merge_layer_def)
#set new feature's geometry
feature.SetGeometry(merge_geometry)
#add new feature to the layer
merge_layer.CreateFeature(feature)