from policies.preprocess.preprocess import *


class Mean(PreProcess):

    def __init__(self):
        PreProcess.__init__()

    def preProcess(self, frameworkObj):
        if (len(frameworkObj.invalids) == 1):
            frameworkObj.invalids.extend([frameworkObj.invalids[0] * len(frameworkObj.data[0])])
        data_new = copy.deepcopy(frameworkObj.data)
        # assume data is just either training or test or val; but this should not know that
        # base functionality to fill in random values for each data field
        avgColumns = list(map(lambda column: sum(column)/len(column), zip(*frameworkObj.data)))
        for i in len(frameworkObj.data):
            for j in len(frameworkObj.data[0]):
                if (frameworkObj.data[i][j] == frameworkObj.invalids[j]):
                    # it is invlalid, a random functionality.
                    data_new[i][j] = avgColumns[j]
                else:
                    data_new[i][j] =frameworkObj.data[i][j]

        return data_new