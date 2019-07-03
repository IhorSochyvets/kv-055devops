from .Employee import Employee

class Developer(Employee):
    def __init__(self, firstName, secondName, experianceValue, salaryValue, higherManager):
        self.higherManager = higherManager
        super(Developer, self).__init__(firstName, secondName, experianceValue, salaryValue)

    def show(self):
        print("Developer Name: {0} {1}; Manager: {2}; Experience: {3} years; ".format(self.firstName, self.secondName, self.higherManager, self.experianceValue))
