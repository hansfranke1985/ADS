import os
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *

# [SC] Supply path to qgis location
QgsApplication.setPrefixPath("C:\OSGeo4W64\apps\qgis", True) # [TODO]

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], True)
# Load providers
qgs.initQgis()

# [SC] load online dataset into a layer via WFS
uri2 = "https://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs"
uri = "https://demo.geo-solutions.it/geoserver/ows?service=WFS&version=1.1.0&request=GetFeature&typename=geosolutions:regioni"
#vlayer = QgsVectorLayer(uri2, "Regions of Italy", "WFS")

# [SC] alternatively load local datafile into a layer
vlayer = QgsVectorLayer("/PdokDataRetriever/retrievedData/provinces.gml", "Regions of Utrecht", "ogr")

QgsProject.instance().addMapLayer(vlayer)

# create a canvas object
canvas = QgsMapCanvas()
# set window title
canvas.setWindowTitle("Map window")
# set the background color for the canvas
canvas.setCanvasColor(Qt.white)
# enable antialiasing in the canvas
canvas.enableAntiAliasing(True)
# show the canvas
canvas.show()

# set the map canvas layer set
canvas.setLayers([vlayer])
# set extent to the extent of our layer
canvas.setExtent(vlayer.extent())
canvas.zoomToFullExtent()


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
exitcode = qgs.exec_()
qgs.exitQgis()
sys.exit(exitcode)