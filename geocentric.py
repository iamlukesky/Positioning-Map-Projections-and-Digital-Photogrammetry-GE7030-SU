'''
Johnnie Hard, 2017
johnnie.hard@gmail.com
Coursework for GE7030, Positioning, Map Projections and Digital Photogrammetry, 7.5 hp
Master's Programme in Geomatics with Remote Sensing and GIS, Stockholm University

Exercise:
From a given lat, lon pair (and height above the ellipsoid), calculate the geocentric XYZ coordinates and then back to lat, lon.

Formulas: http://www.lantmateriet.se/globalassets/kartor-och-geografisk-information/gps-och-matning/geodesi/transformationer/xyz_geodetiska_koord_och_exempel.pdf
'''
from ellipsoid import *

print "\nInitialize grs80 and bessel ellipsoids...\n"
grs80 = Ellipsoid(6378137, 298.257222101)
bessel = Ellipsoid(6377397.155, 299.1528128)

print "Get geocentric X, Y, Z for lat, lon, h coordinates 58, 17, 30...\n"
grs80_geocentric = grs80.getGeocentric(58, 17, 30)
bessel_geocentric = bessel.getGeocentric(58, 17, 30)

print 'grs80: ', 'X', grs80_geocentric[0], 'Y', grs80_geocentric[1], 'Z', grs80_geocentric[2]
print 'bessel: ', 'X', bessel_geocentric[0], 'Y', bessel_geocentric[1], 'Z', bessel_geocentric[2]

print '\nAnd back to lat, lon:\n'

grs80_latlon = grs80.getLatLon(grs80_geocentric)
bessel_latlon = bessel.getLatLon(bessel_geocentric)

print 'grs80: ', grs80_latlon[0], grs80_latlon[1], grs80_latlon[2]
print 'bessel: ', bessel_latlon[0], bessel_latlon[1], bessel_latlon[2]