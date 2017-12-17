#base class for model
class Model:
    def __init__(self):
        pass

    def build(self, frameworkObj, isTest = False):
        # use frameworkObj.data if isTest == False
        # test can call build with isTest = True, and pass a list of lists as second parameter
        pass
