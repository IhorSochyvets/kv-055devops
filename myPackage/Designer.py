from .Developer import Developer

class Designer(Developer):
    def __init__(self, firstName, secondName, experianceValue, salaryValue, higherManager, effCoeff):
        self.effCoeff = effCoeff
        super(Designer, self).__init__(firstName, secondName, experianceValue, salaryValue, higherManager)

    def show(self):
        print("Designer Name: {0} {1}; Manager: {2}; Experience: {3} years; ".format(self.firstName, self.secondName, self.higherManager, self.experianceValue))
