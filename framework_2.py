#from policies.model.knn import *
from policies.model.naiveBayes import *
from policies.normalize.center import *
from policies.test.trainTest import *
from policies.preprocess.mode import *
#from policies.test.kFold import *
import csv

class Framework:
	def __init__(self, data, invalids=(0,), preprocessPolicy=Mode(), normalizePolicy=Center(), modelPolicy=NaiveBayes(),testPolicy=TrainTest()):
		
		memberDict = dict()
		
		memberDict["data"] = data
		memberDict["invalids"] = list(invalids)
		
		
		
		memberDict["preProcess"] = preprocessPolicy.preProcess
		memberDict["normalize"] = normalizePolicy.normalize
		memberDict["build"] = modelPolicy.build
		memberDict["test"] = testPolicy.test
		
		memberDict["model"] = None
		memberDict["accuracy"] = None

		def processData(self):
			self.modelPolicy = self
			self.preProcess(self)  
			self.normalize(self)
			self.model = self.build(self)
			self.accuracy = self.test(self)
			return (self.model, self.accuracy)
		memberDict["processData"] = processData
		
		self.model, self.accuracy = type("newClass", (), memberDict)().processData()

	def processData(self):
		return (self.model, self.accuracy)
if __name__ == "__main__":
	with open("dataset.csv", 'rU') as f:
		reader = csv.reader(f)
		data = list(list(map(float, rec)) for rec in csv.reader(f, delimiter=','))  # reads csv into a list of lists
	framework = Framework(data, invalids = ["nan",0,0,0,0,0,"nan","nan","nan"])
	model, accuracy = framework.processData()
	print(accuracy)
