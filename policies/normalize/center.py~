from policies.normalize.normalize import *

class Center(Normalize):
	def __init__(self):
		Normalize.__init__()
	

	def normalize(self, frameworkObj):
		means = [0] * len(frameworkObj.data[0])

		for row in frameworkObj.data:
			for val in enumerate(row):
				means[val[0]] += val[1]
		numRows = len(data)
		means = list(map(lambda x : x/numRows,means))

		stdDevs = [0] * len(frameworkObj.data[0])
		
		for i in range(len(frameworkObj.data)):
			for j in range(len(frameworkObj.data[0])):
				stdDevs += (frameworkObj.data[i][j] - means[j])**2
		
		stdDevs = list(map(lambda x : (x/(numRows-1))**0.5, stdDevs))

		for i in range(len(frameworkObj.data)):
			for j in range(len(frameworkObj.data[0])):
				frameworkObj.data[i][j] = (frameworkObj.data[i][j] - means[j])/stdDevs[j]

