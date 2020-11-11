# import the WebFeatureService class from the OWSLib library
from owslib.wfs import WebFeatureService

# connects to WFS of the Bestuurlijke Grenzen dataset on PDOK
# link to the dataset: https://www.pdok.nl/downloads/-/article/bestuurlijke-grenzen
#
# url: a string value indicating the URL of the WFS
# version: a string value indicating the version of the WFS;
#       PDOK supporta WFS 2.0.0 but we will use the previous version 1.1.0 that supports the srsname parameter
mywfs = WebFeatureService(url='http://geodata.nationaalgeoregister.nl/bestuurlijkegrenzen/wfs', version='1.1.0')

# list available feature types; in other words, list datasets that can be downloaded from this WFS server
# the expected output: ['bestuurlijkegrenzen:gemeenten', 'bestuurlijkegrenzen:landsgrens', 'bestuurlijkegrenzen:provincies']
# bestuurlijkegrenzen:gemeenten: a region dataset depicting municipalities of the Netherlands
# bestuurlijkegrenzen:landsgrens: a region dataset the national boundaries of the Netherlands
# bestuurlijkegrenzen:provincies: a region dataset depicting provinces of the Netherlands
featureTypes = list(mywfs.contents)
print(featureTypes)

# retrieve the province dataset in GML format
provinceFeatures = mywfs.getfeature(typename='bestuurlijkegrenzen:provincies', srsname='urn:ogc:def:crs:EPSG::28992')
# store the dataset to a local file named "provinces.gml"
with open('retrievedData/provinces.gml', 'wb') as provinceOut:
    provinceOut.write(provinceFeatures.read())

# retrieve the national boundaries dataset in JSON format
boundaryFeatures = mywfs.getfeature(typename='bestuurlijkegrenzen:landsgrens', srsname='urn:ogc:def:crs:EPSG::28992', outputFormat='json')
# store the dataset to the local file named "boundaries.txt"
with open('retrievedData/boundaries.txt', 'wb') as boundaryOut:
    boundaryOut.write(boundaryFeatures.read())

