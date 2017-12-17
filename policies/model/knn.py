from policies.model.model import *
import math


class KNN(Model):
    def __init__(self, k, data):
        Model.__init__()
        self.K = k
        self.trainingData = data

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
        return neighbors

    def distance(self,pt1,pt2):
        distance = 0
        length = len(pt1)
        for x in range(length):
            distance += pow((pt1[x] - pt2[x]), 2)
        return math.sqrt(distance)