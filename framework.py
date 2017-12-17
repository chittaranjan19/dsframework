from policies.model.naiveBayes import *
from policies.normalize.center import *
from policies.test.trainTest import *
from policies.preprocess.mean import *


class Framework:
    def __init__(self, data, invalids = 0, preprocessPolicy=Mean(), normalizePolicy=Center(), modelPolicy=NaiveBayes(),testPolicy=TrainTest()):
        self.data = data
        self.preprocessPolicy = preprocessPolicy
        self.normalizePolicy = normalizePolicy
        self.modelPolicy = modelPolicy
        self.testPolicy = testPolicy

    def setPreprocessPolicy(self, preprocessPolicy):
        self.preprocessPolicy = preprocessPolicy

    def setNormalizePolicy(self, normalizePolicy):
        self.normalizePolicy = normalizePolicy

    def setModelPolicy(self, modelPolicy):
        self.modelPolicy = modelPolicy

    def setTestingPolicy(self, testPolicy):
        self.testPolicy = testPolicy

    def setData(self, data):
        self.data = data

    def processData(self):
        # self.data includes both training and test data, including test data, parameters a little hazy, should decide on the design.
        self.data = self.preprocessPolicy.preProcess(self)  # <- this 'self' being passed should be second param in each of the policies. Use .data to access and transform the data in-place.
        self.normalizePolicy.normalize(self)
        self.model = self.modelPolicy.build(self)
        self.accuracy = self.testPolicy.test(self)
        return (self.model, self.accuracy)
        # we'll decide how to return info to the client later; there needs to be a way he can use the model
