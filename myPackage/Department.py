from .Developer import Developer
from .Designer import Designer

class Department(object):
    def __init__(self, list_of_dev_and_des, list_of_managers):
        self.list_of_dev_and_des = list_of_dev_and_des
        self.list_of_managers = list_of_managers

    def show(self):
        print('List of managers with their own team:')
        for i in range(len(self.list_of_managers)):
            self.list_of_managers[i].show()

    def salary_giving(self):
        n = len(self.list_of_dev_and_des)
        # salary for managers
        for manager in self.list_of_managers:
            b = 0
            s = manager.salaryValue
            if self.more_dev_then_des():        #if team has more then half of developers
                s = s * 1.1
            if 5 < n <= 10:
                b = 200                          #if team has more then 5 employee
            elif n > 10:
                b = 300                          #if team has more then 10 employee
            if manager.experianceValue > 2:
                b = b + 200
            elif manager.experianceValue > 5:
                b = b + 500
                s = s + (s * 1.1)
            print("{0} {1} got salary: {2}".format(manager.firstName, manager.secondName, s + b))

        #salary for developers and designers
        for d in self.list_of_dev_and_des:
            b = 0
            s = d.salaryValue
            if d.experianceValue > 2:
                b = b + 200
            elif d.experianceValue > 5:
                b = b + 500
                s = s * 1.1
            if type(d) is Designer:
                s = s * float(d.effCoeff)
            print("{0} {1} got salary: {2}".format(d.firstName, d.secondName, s + b))

    #returns the number of developers in the team
    def more_dev_then_des(self):
        dev = 0
        for d in self.list_of_dev_and_des:
            if type(d) is Developer:
                dev = dev + 1
        return(dev > (len(self.list_of_dev_and_des)-dev))
