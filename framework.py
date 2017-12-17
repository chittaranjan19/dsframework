from policies.model.model import *
from policies.normalize.normalize import *
from policies.test.testing import *
from policies.preprocess.preprocess import *
import pandas

class Framework:
    def __init__(self, data, preprocesspobj=PreProcess(), normalizepobj=Normalize(), modelpobj=Model(), testpobj=Testing(), invalids = []):
        self.preProcesPObj = preprocesspobj
        self.normalizePObj = normalizepobj
        self.modelPObj = modelpobj
        self.testPObj = testpobj
        self.data = data
        self.invalids = invalids

    def setPreProcecssObj(self,preprocessPObj):
        self.preProcesPObj = preprocessPObj

    def setNormalizePObj(self,normalizePObj):
        self.normalizePObj = normalizePObj

    def setModelPObj(self, modelPObj):
        self.modelPObj = modelPObj

    def setTestingPObj(self,testPObj):
        self.testPObj = testPObj


    def processData(self,data,invalids=[0]):
        #self.data includes both training and test data, including test data, parameters a little hazy, should decide on the design.
        data = self.preProcesPObj.preProcess(data,invalids)
        data = self.normalizePObj.normalize(data)
        res = self.modelPObj.classify(data)
        return self.testPObj.test(data, res)


if __name__ == "__main__":
    data = pandas.read_csv("pima-indians-diabetes.data")
    print(list(data))
    framework = Framework(data,invalids=[0])