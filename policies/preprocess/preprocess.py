import random,copy
#base class for preprocess policy, fill in missing values
class PreProcess:
    def __init__(self):
        pass

    def preProcess(self, data, invalids):
        if (len(self.invalids) == 1):
            self.invalids.extend([self.invalids[0] * len(self.data[0])])
        data_new = copy.deepcopy(data)
        #assume data is just either training or test or val; but this should not know that
        #base functionality to fill in random values for each data field
        minColumns = self.findMinOfColumns(data)
        maxColumns = self.findMaxOfColumns(data)
        for i in len(data):
            for j in len(data[0]):
                if(data[i][j] == invalids[j]):
                    #it is invlalid, a random functionality.
                    data_new[i][j] = random.randint(minColumns[j],maxColumns[j])
                else:
                    data_new[i][j] = data[i][j]

        return data_new

    def findMinOfColumns(self,data):
         return list(map(min, zip(*data)))

    def findMaxOfColumns(self,data):
        return list(map(max, zip(*data)))