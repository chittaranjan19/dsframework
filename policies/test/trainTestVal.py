from policies.test.testing import *
import copy

class TrainTestVal(Testing):
    def __init__(self):
        Testing.__init__()

    def test(self, frameworkObj):
        #randomise data
        data = copy.deepcopy(frameworkObj.data)
        splitPerc = 0.7
        data_new = data[:splitPerc*len(data)],data[splitPerc*(len(data)):(1-splitPerc)*len(data)], data[(1-splitPerc)*(len(data)):]
        return data_new

