# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:55:07 2020

@author: hansf
"""

from pcraster import * 
print("loading packages ok")

import os 
print(os.getcwd())

#change directory to map folder
os.chdir(r"C:\Users\hansf\Documents\GitHub\ADS\SpatialData\week_4\Lab_MapAlgebra\mapalgebra")
print(os.getcwd())

#load a map
waterMap=readmap("water.map") 
#visualize the map
aguila(waterMap)

#loading another map
isroadMap = readmap("isroad.map")

aguila(waterMap, isroadMap)

#load another map
topoMap = readmap("topo.map")
aguila(topoMap)

#Question 1.1.3
buildMap = readmap("buildg.map")
aguila(buildMap)
##Nominal, building is classified with no order


#load all maps
exec(open("openmaps.py").read())

#Point operations

resultMap = slope(topoMap) * (1 + phreaticMap)
aguila(resultMap)

#Quantitative computation with scalar maps
unsatMap = topoMap - phreaticMap
aguila(unsatMap)

infilMap = soilsMap * unsatMap
aguila(infilMal)


#Boolean operators
#test where road and water = bridge
isbridgeMap = isroadMap & iswaterMap
aguila(isroadMap, iswaterMap, isbridgeMap)


## Comparison operators = boolans maps
highMap = topoMap > 40
aguila(topoMap, highMap)

isMineMap = buildgMap == 5
aguila(buildMap, isMineMap)

toponewMap = ifthenelse(isMineMap, topoMap-20, topoMap)



lowestPointOnTopoNew = mapminimum(toponewMap)
lowestPointOnTopoNew

# 1.3 Area Operations

soiltopoMap = areaaverage(topoMap, soilsMap)
aguila(soiltopoMap, topoMap, soilsMap)


soilareaMap = areaarea(soilsMap)
aguila(soilareaMap, soilsMap)

aguila(treesMap)

pineMap = treesMap == 1
aguila(pineMap)
pineclumMap = clump(pineMap)
aguila(pineclumMap)


pineareaMap = areaarea(pineclumMap)
aguila(pineareaMap)


pineare2Map = ifthenelse(pineMap, pineareaMap, 0)
aguila(pineare2Map)

pineMap = treesMap == 1

pineclumMap = clump(pineMap)

pineareaMap = areaarea(pineclumMap)

pineare2Map = ifthenelse(pineMap, pineareaMap, 0)

contMap = pineare2Map > (4 * 100 * 100)

aguila(contMap)





















