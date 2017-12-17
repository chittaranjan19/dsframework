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
		INTERVALS = 10
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
				self.probs[(i,(diff/INTERVALS) + (j-1)*INTERVALS,(diff/INTERVALS) + (j)*INTERVALS, 0 )] = 0	
				self.probs[(i,(diff/INTERVALS) + (j-1)*INTERVALS,(diff/INTERVALS) + (j)*INTERVALS, 1 )] = 0
		self.probs[1] = 0
		self.probs[0] = 0

		for i in range(len(data)):
			for j in range(len(data[0]) - 1):
				for key in self.probs:
					print(key,self.probs[key])
					if key[0] == j and data[i][j] > key[1] and data[i][j] < key[2] and data[i][-1] == key[-1]:
						self.probs[key] += 1
		
				self.probs[data[i][-1]] += 1		
		self.probs["prob1"] = self.probs[0]/len(self.data)
		self.probs["prob0"] = self.probs[1]/len(self.data)
		
		for key in probs:
			if key not in [0,1,"prob0","prob1"]:
				self.probs[key] = (self.probs[key] + 1)/ self.probs[key[-1]] + INTERVALS				
		
		return self
	def classify(self, query):
		pos = 1; neg = 1
		for i in range(len(query)):
			try:
				neg = neg * self.probs[(i, query[i]//self.INTERVALS, query[i]//self.INTERVALS + self.INTERVALS,0)]
			except:
				neg = neg * 1/(self.probs[0] + self.INTERVALS)
			try:
				pos = pos * self.probs[(i, query[i]//self.INTERVALS, query[i]//self.INTERVALS + self.INTERVALS,1)]
			except:
				pos = pos * 1/(self.probs[1] + self.INTERVALS)
		pos *= self.probs["prob1"]
		neg *= self.probs["prob0"]
		return 1 if pos >= neg else 0
