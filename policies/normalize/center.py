from policies.normalize.normalize import *

class Center(Normalize):
	def __init__(self):
		Normalize.__init__()
	

	def normalize(self):
		means = [0] * len(self.data[0])

		for row in self.data:
			for val in enumerate(row):
				means[val[0]] += val[1]
		numRows = len(data)
		means = list(map(lambda x : x/numRows,means))

		stdDevs = [0] * len(self.data[0])
		
		for i in range(len(self.data)):
			for j in range(len(self.data[0])):
				stdDevs += (self.data[i][j] - means[j])**2
		
		stdDevs = list(map(lambda x : (x/(numRows-1))**0.5), stdDevs)

		for i in range(len(self.data)):
			for j in range(len(self.data[0])):
				self.data[i][j] = (self.data[i][j] - means[j])/stdDevs[j]

