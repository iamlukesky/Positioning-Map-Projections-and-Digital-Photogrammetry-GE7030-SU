from math import *

def greatCircleDistance(dep, dest, earthRadius = 6371.0): #[lat, lon], radius in km
	dep = map(radians, dep)
	dest = map(radians, dest)
	ld = abs(dep[1] - dest[1]) #lonigtude differential
	angle = acos(sin(dep[0]) * sin(dest[0]) + cos(dep[0]) * cos(dest[0]) * cos(ld))
	arclen = arcLength(earthRadius, angle)
	return arclen

def arcLength(r, theta):
	return r * theta

stockholm = [59.3, 18.05]
seattle = [47.6, -112.3]

distance = greatCircleDistance(stockholm, seattle)
print distance