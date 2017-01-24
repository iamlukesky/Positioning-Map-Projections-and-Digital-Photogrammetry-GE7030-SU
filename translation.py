
import numpy as np
from math import *

class Translate:

	def __init__(self, direction):
		self.delta = {
			"X": -419.375 * direction,
			"Y": -99.253 * direction,
			"Z": -591.349 * direction
		}

		self.omega = {
			"x": radians(0.850458 / 3600) * direction,
			"y": radians(1.817245 / 3600) * direction,
			"z": radians(-7.862245 / 3600) * direction
		}

		self.deltaScale = 1 * direction + 0.99496 / 1000000

		# formula
		self.rZ = [[cos(self.omega["z"]), sin(self.omega["z"]), 0],
			       [-sin(self.omega["z"]), cos(self.omega["z"]), 0],
			       [0, 0, 1]]

		self.rY = [[cos(self.omega["y"]), 0, -sin(self.omega["y"])],
			       [0, 1, 0],
			  	   [sin(self.omega["y"]), 0, cos(self.omega["y"])]]

		self.rX = [[1, 0, 0],
			  	   [0, cos(self.omega["x"]), sin(self.omega["x"])],
			       [0, -sin(self.omega["x"]), cos(self.omega["x"])]]

		self.rZ = np.matrix(self.rZ)
		self.rY = np.matrix(self.rY)
		self.rX = np.matrix(self.rX)

		self.r = self.rZ * self.rY * self.rX

		self.deltaM = np.matrix([[self.delta["X"]], [self.delta["Y"]], [self.delta["Z"]]])

	def translate(self, geocentric):
		inputs = np.matrix(geocentric).reshape(3, 1)
		result = self.deltaM + self.deltaScale * self.r * inputs
		return np.squeeze(np.asarray(result))

# [3240036.3696, 990578.5272, 5385763.1648] #SWEREF 93

# []