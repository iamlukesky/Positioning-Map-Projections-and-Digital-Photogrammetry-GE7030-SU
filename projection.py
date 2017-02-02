from ellipsoid import *
from math import *

# SWEREF99TM
sweref99tm = {
	'medelMeridian': 15.0,
	'refLat': 0.0,
	'kNoll': 0.9996,
	'falseEasting': 500000.0,
	'falseNorthing': 0.0,
	'ellipsoid': Ellipsoid(6378137, 298.257222101) #GRS80
}

# Testkoordinater
testcoords = {
	'lat': 59.3,
	'lon': 18.05
}

lat = testcoords['lat']
lon = testcoords['lon']

# Coefficents for getting iso lat
A = sweref99tm['ellipsoid'].eSq
B = (1.0 / 6.0) * ((5.0 * sweref99tm['ellipsoid'].e ** 4) - sweref99tm['ellipsoid'].e ** 6)
C = (1.0 / 120.0) * ((104.0 * sweref99tm['ellipsoid'].e ** 6) - (45.0 * sweref99tm['ellipsoid'].e ** 8))
D = (1.0 / 1260.0) * (1237.0 * sweref99tm['ellipsoid'].e ** 8)

def isoLat(lat, lon):
	lat = radians(lat)
	lon = radians(lon)
	return lat - sin(lat) * cos(lat) * ( A + B * sin(lat) ** 2 + C * sin(lat) ** 4 + D * sin(lat) ** 6 )

def deltaLambda(lon):
	return radians(lon - sweref99tm['medelMeridian']) # returnera som radians?

def getEtaPrim(isoLat, deltaLambda):
	return atanh(cos(isoLat) * sin(deltaLambda))

def getXiPrim(isoLat, deltaLambda):
	return atan(tan(isoLat) / cos(deltaLambda))

# Coefficients for getting planar coordinates
n = sweref99tm['ellipsoid'].n
beta1 = ((1.0 / 2.0) * n) - ((2.0 / 3.0) * n ** 2) + ((5.0 / 16.0) * n ** 3) + ((41.0 / 180.0) * n ** 4)
beta2 = ((13.0 / 48.0) * n ** 2) - ((3.0 / 5.0) * n ** 3) + ((557.0 / 1440.0) * n ** 4)
beta3 = ((61.0 / 240.0) * n ** 3) - ((103.0 / 140.0) * n ** 4)
beta4 = ((49561.0 / 161280.0) * n ** 4)
aHat = sweref99tm['ellipsoid'].aHat
falseEasting = sweref99tm['falseEasting']

def getPlanar(lat, lon):
	etaPrim = getEtaPrim(isoLat(lat, lon), deltaLambda(lon))
	xiPrim = getXiPrim(isoLat(lat, lon), deltaLambda(lon))

	# x = N
	# y = E

	N = sweref99tm['falseNorthing'] + sweref99tm['kNoll'] * aHat * ( xiPrim + \
		beta1 * sin(2 * xiPrim) * cosh(2 * etaPrim) + \
		beta2 * sin(4 * xiPrim) * cosh(4 * etaPrim) + \
		beta3 * sin(6 * xiPrim) * cosh(6 * etaPrim) + \
		beta4 * sin(8 * xiPrim) * cosh(8 * etaPrim)) 

	E = falseEasting + sweref99tm['kNoll'] * aHat * ( etaPrim + \
		beta1 * cos(2 * xiPrim) * sinh(2 * etaPrim) + \
		beta2 * cos(4 * xiPrim) * sinh(4 * etaPrim) + \
		beta3 * cos(6 * xiPrim) * sinh(6 * etaPrim) + \
		beta4 * cos(8 * xiPrim) * sinh(8 * etaPrim)) 

	return [N, E]

print "my result: ", getPlanar(lat, lon)
print "expected:  ", [6577433.873, 673663.603]

