from policies.test.testing import *
import copy
from random import shuffle

class KFold(Testing):
    def __init__(self):
        Testing.__init__(self)
        self.K = 10

    def test(self, frameworkObj):
        data = copy.deepcopy(frameworkObj.data)
        shuffle(data)
        percAccuracy = 0
        modeledObj = frameworkObj.modelPolicy.build(data, True)
        for train,test in self.genKFolds(data):
            modeledObj = frameworkObj.modelPolicy.build(train,True)
            numCorrect = 0
            for instance in test:
                output = modeledObj.classify(instance[:-1])
                if(output == instance[-1]):
                    numCorrect +=1
            percAccuracy += (float(numCorrect)/len(test))*100

        return modeledObj, float(percAccuracy)/self.K

    def genKFolds(self, data):
        for k in xrange(self.K):
            #k-1 for train, k for test
            training = [x for i, x in enumerate(data) if i % self.K != k]
            validation = [x for i, x in enumerate(data) if i % self.K == k]
            yield training, validation