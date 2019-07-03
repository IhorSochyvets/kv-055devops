from .Employee import Employee

class TopManager(Employee):
    def __init__(self, firstName, secondName, experianceValue, salaryValue):
        super(TopManager, self).__init__(firstName, secondName, experianceValue, salaryValue)

    def show(self):
        print("CIO Name: {0} {1};".format(self.firstName, self.secondName))
