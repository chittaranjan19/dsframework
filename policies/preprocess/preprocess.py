import random,copy
#base class for preprocess policy, fill in missing values
class PreProcess:
    def __init__(self):
        pass

    def preProcess(self, frameworkObj):
        if (len(frameworkObj.invalids) == 1):
            frameworkObj.extend([frameworkObj.invalids[0] * len(frameworkObj.data[0])])
        data_new = copy.deepcopy(frameworkObj.data)
        #assume data is just either training or test or val; but this should not know that
        #base functionality to fill in random values for each data field
        minColumns = self.findMinOfColumns(frameworkObj.data)
        maxColumns = self.findMaxOfColumns(frameworkObj.data)
        for i in len(frameworkObj.data):
            for j in len(frameworkObj.data[0]):
                if(frameworkObj.data[i][j] == frameworkObj.invalids[j]):
                    #it is invlalid, a random functionality.
                    data_new[i][j] = random.randint(minColumns[j],maxColumns[j])
                else:
                    data_new[i][j] = frameworkObj.data[i][j]

        return data_new

    def findMinOfColumns(self,data):
         return list(map(min, zip(*data)))

    def findMaxOfColumns(self,data):
        return list(map(max, zip(*data)))