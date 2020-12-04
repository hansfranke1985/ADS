origin_layer =  QgsProject.instance().mapLayersByName('PC4_center')[0]
destination_layer =  QgsProject.instance().mapLayersByName('policestations_ams_2013')[0]
matrix =  QgsProject.instance().mapLayersByName('nearest_police2')[0]
destination_expr = QgsExpression('origin_id=176')
print("works")
for f in matrix.getFeatures(QgsFeatureRequest(destination_expr)):
    print("works")
    origin_expr = QgsExpression('Postcode4={}'.format(f['destinatio']))
    print("works")
    destination_expr = QgsExpression('OBJECTID={}'.format(f['origin_id']))
    print("works")
    origin_feature = origin_layer.getFeatures(QgsFeatureRequest(origin_expr))
    print("works")
    origin_coords =  [(f.geometry().asPoint().x(), f.geometry().asPoint().y())
        for f in origin_feature]
    print(origin_coords)
    destination_feature = destination_layer.getFeatures(QgsFeatureRequest(destination_expr))
    destination_coords =  [(f.geometry().asPoint().x(), f.geometry().asPoint().y())
        for f in destination_feature]
    params = {
        'INPUT':'C:\\Users\\hansf\\Documents\\GitHub\\ADS\\SpatialData\\week_3_&_Half\\Lab3.3\\Lab 3.3 data\\roads_ams_2008.shp',
        'START_POINT':'{},{}'.format(origin_coords[0][0], origin_coords[0][1]),
        'END_POINT':'{},{}'.format(destination_coords[0][0], destination_coords[0][1]),
        'STRATEGY':1,
        'ENTRY_COST_CALCULATION_METHOD':1,
        'DIRECTION_FIELD':'DIRECTIONA',
        'VALUE_FORWARD':'One Way (Digitizing direction)\n',
        'VALUE_BACKWARD':'One way (Against digitizing direction)\n',
        'VALUE_BOTH':'',
        'DEFAULT_DIRECTION':2,
        'SPEED_FIELD':'kph',
        'DEFAULT_SPEED':5,
        'TOLERANCE':0,
        'OUTPUT':'memory:'}
    print('Executing analysis')
    processing.runAndLoadResults("qneat3:shortestpathpointtopoint", params)