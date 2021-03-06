from policies.model.model import *
import math


class KNN(Model):
    def __init__(self):
        Model.__init__(self)
        self.K = 3

    def setData(self,data):
        self.data = data
    def build(self, frameworkObj, isTest = False):
        if isTest:
            self.trainingData = frameworkObj
        else:
            self.trainingData = frameworkObj.data
        return self
    def classify(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(self.trainingData)):
            dist = self.distance(testInstance, self.trainingData[x])
            distances.append((self.trainingData[x], dist))
        distances.sort(key=lambda x:x[1])
        neighbors = []
        for x in range(self.K):
            neighbors.append(distances[x][0])
        return 1 if sum(map(lambda val : val[-1],neighbors)) > self.K/2.0 else 0

    def distance(self,pt1,pt2):
        distance = 0
        length = len(pt1)
        for x in range(length):
            distance += pow((pt1[x] - pt2[x]), 2)
        return math.sqrt(distance)
