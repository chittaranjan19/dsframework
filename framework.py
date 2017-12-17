from policies.model.NaiveBayes import *
from policies.normalize.Center import *
from policies.test.TrainTestVal import *
from policies.preprocess.Mean import *


class Framework:
    def __init__(self, data, preprocessPolicy=Mean(), normalizePolicy=Center(), modelPolicy=NaiveBayes(), testPolicy=TrainTestVal()):
        self.data = data
        self.preprocessPolicy = preprocessPolicy.setData(data)
        self.normalizePolicy = normalizePolicy.setData(data)
        self.modelPolicy = modelPolicy.setData(data)
        self.testPolicy = testPolicy.setData(data)

    def setPreprocessPolicy(self,preprocessPolicy):
        self.preprocessPolicy = preprocessPolicy.setData(self.data)

    def setNormalizePolicy(self,normalizePolicy):
        self.normalizePolicy = normalizePolicy.setData(self.data)

    def setModelPolicy(self, modelPolicy):
        self.modelPolicy = modelPolicy.setData(self.data)

    def setTestingPolicy(self,testPolicy):
        self.testPolicy = testPolicy.setData(self.data)


    def processData(self):
        #self.data includes both training and test data, including test data, parameters a little hazy, should decide on the design.
        self.preprocessPolicy.preProcess()
        self.normalizePolicy.normalize()
        self.modelPolicy.classify()
        self.testPolicy.test()
        
        #we'll decide how to return info to the client later; there needs to be a way he can use the model
