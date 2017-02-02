
'''
Define an ellipsoid by its semi major axis (a) and flattening (f).
The definition of the ellipsoid is then saved in the instance object and the functions can be called with just the coordinates to be transformed.
'''

from math import *

class Ellipsoid:
	def __init__(self, a, f):
		self.a = a
		self.f = 1/f
		self.eSq = self.geteSquared(self.f)
		self.e = sqrt(self.eSq)
		self.n = self.getN(self.f)
		self.aHat = self.getAHat(self.a, self.n)

	def getX(self, lat, lon, h):
		return (self.getNprime(lat) + h) * cos(radians(lat)) * cos(radians(lon))

	def getY(self, lat, lon, h):
		return (self.getNprime(lat) + h) * cos(radians(lat)) * sin(radians(lon))

	def getZ(self, lat, h):
		return (self.getNprime(lat) * (1 - self.eSq) + h) * sin(radians(lat))

	def getGeocentric(self, lat, lon, h):
		return [self.getX(lat, lon, h), self.getY(lat, lon, h), self.getZ(lat, h)]

	def getNprime(self, lat):
		return self.a / sqrt(1 - self.eSq * pow(sin(radians(lat)), 2))

	def getN(self, f):
		return f / (2 - f)

	def geteSquared(self, f):
		return f * (2 - f)

	def getAHat(self, a, n):
		return a / (1 + n) * (1 + ((1.0 / 4.0) * n ** 2 ) + ((1.0 / 64.0) * n ** 4))

	def getLatLon(self, geocentric):
		lon = degrees(atan(geocentric[1] / geocentric[0]))
		p = sqrt((geocentric[0]**2) + (geocentric[1]**2))
		theta = degrees(atan((geocentric[2]) / (p * sqrt(1 - self.eSq))))
		# prep for lat
		inner_division = (self.a * self.eSq) / (sqrt(1 - self.eSq))
		above_division = geocentric[2] + inner_division * (sin(radians(theta)) ** 3)
		#below division
		below_division = p - self.a * self.eSq * (cos(radians(theta)) ** 3)
		lat = degrees(atan(above_division / below_division))
		h = ((p) / (cos(radians(lat)))) - self.getNprime(lat)
		return [lat, lon, h]