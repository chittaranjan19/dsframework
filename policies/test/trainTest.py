from policies.test.testing import *
import copy
from random import shuffle

class TrainTest(Testing):
    def __init__(self):
        Testing.__init__(self)

    def test(self, frameworkObj):
        #randomise data
        data = copy.deepcopy(frameworkObj.data)
        shuffle(data)
        splitPerc = 0.7
        train_data, test_data = data[:int(splitPerc*len(data))], data[int(splitPerc*len(data)):]
        modeledObj = frameworkObj.modelPolicy.build(train_data,True)
        numCorrect = 0
        for instance in test_data:
            output = modeledObj.classify(instance[:-1])
            if(output == instance[-1]):
                numCorrect +=1
        percAccuracy = (numCorrect/float(len(test_data)))*100
        return percAccuracy

