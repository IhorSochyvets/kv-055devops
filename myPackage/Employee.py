class Employee(object):
    def __init__(self, firstName, secondName, experianceValue, salaryValue):
        self.firstName = firstName #each employee has: first name, second name, salary, experiance (years)
        self.secondName = secondName
        self.salaryValue = salaryValue
        self.experianceValue = experianceValue

    def show(self):
        print("Employee First and Last Name: {0} {1}; Experience: {2} years; Salary: {3}$".format(self.firstName, self.secondName, self.experianceValue, self.salaryValue))
