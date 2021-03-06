from policies.model.model import *

class NaiveBayes(Model):
	def __init__(self):
		Model.__init__(self)
	
	def build(self, frameworkObj, isTest = False):
		
		if isTest:
			data = frameworkObj
		else:
			data = frameworkObj.data
		
		self.probs = dict()
		INTERVALS = 50
		self.INTERVALS = INTERVALS
		mins = data[0]
		maxs = data[0]
		
		for i in range(len(data)):
			for j in range(len(data[0]) - 1):
				if data[i][j] < mins[j] : mins[j] = data[i][j]
				if data[i][j] > maxs[j] : maxs[j] = data[i][j]

		for i in range(len(data[0]) - 1 ):
			diff = maxs[i] - mins[i]
			for j in range(INTERVALS):
				self.probs[(i,int((diff/INTERVALS) + (j-1)*INTERVALS),int((diff/INTERVALS) + (j)*INTERVALS), 0 )] = 0	
				self.probs[(i,int((diff/INTERVALS) + (j-1)*INTERVALS),int((diff/INTERVALS) + (j)*INTERVALS), 1 )] = 0
		self.probs[1] = 0
		self.probs[0] = 0

		for i in range(len(data)):
			for j in range(len(data[0]) - 1):
				for key in self.probs:
					if key not in [0,1]:
						if key[0] == j and data[i][j] >= key[1] and data[i][j] <= key[2] and data[i][-1] == key[-1]:
							self.probs[key] += 1
		
			self.probs[int(data[i][-1])] += 1		
		self.probs["prob0"] = self.probs[0]/len(data)
		self.probs["prob1"] = self.probs[1]/len(data)
		

		for key in self.probs:
			if key not in [0,1,"prob0","prob1"]:
				self.probs[key] = (self.probs[key] + 1)/ (self.probs[key[-1]] + INTERVALS)				
		return self
	def classify(self, query):
		pos = self.probs["prob1"]; neg = self.probs["prob0"]
		for i in range(len(query)):
			try:
				
				neg = neg * self.probs[(i, (query[i]//self.INTERVALS)*self.INTERVALS, (query[i]//self.INTERVALS)*self.INTERVALS + self.INTERVALS,0)]
			except:
				neg = neg * (1/(self.probs[0] + self.INTERVALS))
			try:
				
				pos = pos * self.probs[(i, (query[i]//self.INTERVALS)*self.INTERVALS, (query[i]//self.INTERVALS)*self.INTERVALS + self.INTERVALS,1)]
			except:
				pos = pos * (1/(self.probs[1] + self.INTERVALS))
			
		return 1 if pos >= neg else 0
