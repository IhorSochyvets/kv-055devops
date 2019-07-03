from .Developer import Developer

class Manager(Developer):
    def __init__(self, firstName, secondName, experianceValue, salaryValue, higherManager, team):
        self.team = team
        super(Manager, self).__init__(firstName, secondName, experianceValue, salaryValue, higherManager)

    def show(self):
        print("Manager Name: {0} {1}; Manager: {2}; Experience: {3} years; ".format(self.firstName, self.secondName, self.higherManager, self.experianceValue))
