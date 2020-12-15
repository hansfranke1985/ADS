# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:41:08 2020

@author: hansf
"""

from pcraster import * 
print("loading packages ok")

import os 
print(os.getcwd())

#change directory to map folder
os.chdir(r"C:\Users\hansf\Documents\GitHub\ADS\SpatialData\week_4\Lab_DinModelling\dynmod\snowmelt")
print(os.getcwd())

#load all maps
anAreaMap = readmap("anArea.map")
demMap = readmap("dem.map")

aguila(demMap,anAreaMap)
#Questions


#2.1. Visualisation of spatio-temporal data

#2.1.1. Static data

dem = readmap("dem.map")
slopemap = slope(dem)
aguila(slopemap)

dem = readmap("dem.map")
slopemap = slope("dem.map")
aguila(demMap,anAreaMap)
aguila(slopemap)


#2.1.2. Temporal spatial data
# Ok

#2.1.3. Temporal non-spatial data
#ok


#2.2. The dynamic modelling framework

#2.2.1. The dynamic modelling class
#2.2.2. Modelling with feedback
#2.3. Reading and writing spatio-temporal data
#2.3.1. Reading and writing static spatial data
#2.3.2. Reading and writing temporal spatial data
#2.3.3. Reading timeseries
#2.4. Point operations: a snow melt model
#2.4.1. Precipitation and temperature
#2.4.2. The snow store
#2.4.3. Runoff generation
#2.5. Neighbourhood operations with defined topology: the snow melt model
#2.5.1. The local drain direction map
#2.5.2. Drain all runoff within one time step: the accuflux function