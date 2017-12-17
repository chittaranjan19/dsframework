from policies.normalize.normalize import *

class Squash(Normalize):
	def __init__(self):
		Normalize.__init__(self)
	

	def normalize(self, frameworkObj):
		mins = frameworkObj.data[0]
		maxs = frameworkObj.data[0]
		
		for i in range(len(frameworkObj.data)):
			for j in range(len(frameworkObj.data[0]) - 1):
				if frameworkObj.data[i][j] < mins[j] : mins[j] = frameworkObj.data[i][j]
				if frameworkObj.data[i][j] > maxs[j] : maxs[j] = frameworkObj.data[i][j]

		for i in range(len(frameworkObj.data)):
			for j in range(len(frameworkObj.data[0]) - 1):
				frameworkObj.data[i][j] = (frameworkObj.data[i][j] - mins[j]) / (maxs[j] - mins[j])
