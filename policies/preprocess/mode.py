from policies.preprocess.preprocess import *
import copy

class Mode(PreProcess):

    def __init__(self):
        PreProcess.__init__(self)

    def preProcess(self, frameworkObj):
        if (len(frameworkObj.invalids) == 1):
            frameworkObj.invalids.extend([frameworkObj.invalids[0]] * len(frameworkObj.data[0]))
        data_new = copy.deepcopy(frameworkObj.data)
        # assume data is just either training or test or val; but this should not know that
        # base functionality to fill in random values for each data field
        modeColumns = list(map(lambda x : max(set(x), key=x.count), zip(*frameworkObj.data)))
        for i in range(len(frameworkObj.data)):
            for j in range(len(frameworkObj.data[0]) - 1):
                if (frameworkObj.data[i][j] == frameworkObj.invalids[j]):
                    # it is invlalid, a random functionality.
                    data_new[i][j] = modeColumns[j]
                else:
                    data_new[i][j] = frameworkObj.data[i][j]

        frameworkObj.data = data_new
