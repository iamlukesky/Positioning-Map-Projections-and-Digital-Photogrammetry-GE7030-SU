
import numpy as np
from math import *
from ellipsoid import *

# constants
delta = {
	"X": -419.375,
	"Y": -99.253,
	"Z": -591.349
}

omega = {
	"x": radians(0.850458 / 3600),
	"y": radians(1.817245 / 3600),
	"z": radians(-7.862245 / 3600)
}

deltaScale = 1 + 0.99496 / 1000000


# formula
rZ = [[cos(omega["z"]),  sin(omega["z"]),  0],
	  [-sin(omega["z"]), cos(omega["z"]),  0],
	  [0,				 0,				   1]]

rY = [[cos(omega["y"]),  0,                -sin(omega["y"])],
	  [0,				 1,				   0],
	  [sin(omega["y"]),  0,                cos(omega["y"])]]

rX = [[1,				 0,				   0],
	  [0,				 cos(omega["x"]),  sin(omega["x"])],
	  [0,				 -sin(omega["x"]), cos(omega["x"])]]


rZ = np.matrix(rZ)
rY = np.matrix(rY)
rX = np.matrix(rX)

r = rZ * rY * rX

deltaM = np.matrix([[delta["X"]], [delta["Y"]], [delta["Z"]]])

inputs = np.matrix([[3240036.3696],
					[990578.5272],
					[5385763.1648]])

output = deltaM + deltaScale * r * inputs

print output