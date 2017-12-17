from policies.preprocess.preprocess import *


class Mode(PreProcess):

    def __init__(self):
        PreProcess.__init__()

    def preProcess(self, data, invalids):
        if (len(self.invalids) == 1):
            self.invalids.extend([self.invalids[0] * len(self.data[0])])
        data_new = copy.deepcopy(data)
        # assume data is just either training or test or val; but this should not know that
        # base functionality to fill in random values for each data field
        modeColumns = list(map(lambda x : max(set(x), key=x.count), zip(*data)))
        for i in len(data):
            for j in len(data[0]):
                if (data[i][j] == invalids[j]):
                    # it is invlalid, a random functionality.
                    data_new[i][j] = avgColumns[j]
                else:
                    data_new[i][j] = data[i][j]

        return data_new