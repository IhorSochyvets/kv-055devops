#Create structure for department:
#There are 3 types of employee: developer, designer and manager
#Each employee has: first name, second name, salary, experiance (years)
#Each designer, developer or manager can have higher managers
#Each designer has effectivness coefficient(0-1)
#Each manager has team of developers and designers.
#Department should have list of managers(which have their own teams)
#Department should be able to give salary (for each employee message: "@firstName@ @secondName@: got salary: @salaryValue@")
#Each employee gets the salary, defined in field Salary. If experiance of employee is > 2 years, he gets bonus + 200$, if experiance is > 5 years, he gets salary*1.2 + bonus 500
#Each designer gets the salary = salary*effCoeff
#Each manager gets salary +
#200$ if his team has >5 members
#300$ if his team has >10 members
#salary*1.1 if more than half of team members are developers.
#Redefine string representation for employee as follows: "@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"

class Employee(object):
    def __init__(self, firstName, secondName, experianceValue, salaryValue):
        self.firstName = firstName #each employee has: first name, second name, salary, experiance (years)
        self.secondName = secondName
        self.salaryValue = salaryValue
        self.experianceValue = experianceValue

    def show(self):
        print("Employee First and Last Name: {0} {1}; Experience: {2} years; Salary: {3}$".format(self.firstName, self.secondName, self.experianceValue, self.salaryValue))

class Developer(Employee):
    def __init__(self, firstName, secondName, experianceValue, salaryValue, higherManager):
        self.higherManager = higherManager
        super(Developer, self).__init__(firstName, secondName, experianceValue, salaryValue)

    def show(self):
        print("Developer Name: {0} {1}; Manager: {2}; Experience: {3} years; ".format(self.firstName, self.secondName, self.higherManager, self.experianceValue))

class Designer(Developer):
    def __init__(self, firstName, secondName, experianceValue, salaryValue, higherManager, effCoeff):
        self.effCoeff = effCoeff
        super(Designer, self).__init__(firstName, secondName, experianceValue, salaryValue, higherManager)

    def show(self):
        print("Designer Name: {0} {1}; Manager: {2}; Experience: {3} years; ".format(self.firstName, self.secondName, self.higherManager, self.experianceValue))

class Manager(Developer):
    def __init__(self, firstName, secondName, experianceValue, salaryValue, higherManager, team):
        self.team = team
        super(Manager, self).__init__(firstName, secondName, experianceValue, salaryValue, higherManager)

    def show(self):
        print("Manager Name: {0} {1}; Manager: {2}; Experience: {3} years; ".format(self.firstName, self.secondName, self.higherManager, self.experianceValue))

class TopManager(Employee):
    def __init__(self, firstName, secondName, experianceValue, salaryValue):
        super(TopManager, self).__init__(firstName, secondName, experianceValue, salaryValue)

    def show(self):
        print("CIO Name: {0} {1};".format(self.firstName, self.secondName))


class Team(object):
    def __init__(self, list_of_dev_and_des):
        self.list_of_dev_and_des = list_of_dev_and_des

    def show(self):
        print('Team:')
        for i in range(len(self.list_of_dev_and_des)):
            self.list_of_dev_and_des[i].show()

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
        for i in range(len(self.list_of_managers)):
            b = 0
            s = self.list_of_managers[i].salaryValue
            if self.more_dev_then_des():        #if team has more then half of developers
                s = s * 1.1
            if 5 < n <= 10:
                b = 200                          #if team has more then 5 employee
            elif n > 10:
                b = 300                          #if team has more then 10 employee
            if self.list_of_managers[i].experianceValue > 2:
                b = b + 200
            elif self.list_of_managers[i].experianceValue > 5:
                b = b + 500
                s = s + (s * 1.1)
            print("{0} {1} got salary: {2}".format(self.list_of_managers[i].firstName, self.list_of_managers[i].secondName, s + b))

        #salary for developers and designers
        for i in range(len(self.list_of_dev_and_des)):
            b = 0
            s = self.list_of_dev_and_des[i].salaryValue
            if self.list_of_dev_and_des[i].experianceValue > 2:
                b = b + 200
            elif self.list_of_dev_and_des[i].experianceValue > 5:
                b = b + 500
                s = s * 1.1
            if type(self.list_of_dev_and_des[i]) is Designer:
                s = s * float(self.list_of_dev_and_des[i].effCoeff)
            print("{0} {1} got salary: {2}".format(self.list_of_dev_and_des[i].firstName, self.list_of_dev_and_des[i].secondName, s + b))


    #returns the number of developers in the team
    def more_dev_then_des(self):
        dev = 0
        for i in range(len(self.list_of_dev_and_des)):
            if type(self.list_of_dev_and_des[i]) is Developer:
                dev = dev + 1
        return(dev > (len(self.list_of_dev_and_des)-dev))



#team1
#Developers
name1 = "Oliver"
lastname1 = "Smith"
exper1 = 2
salary1 = 1000

name2 = "Noah"
lastname2 = "Williams"
exper2 = 3
salary2 = 1200

name3 = "James"
lastname3 = "Jones"
exper3 = 4
salary3 = 1400

#Designer
name4 = "Jack"
lastname4 = "Brown"
exper4 = 4
salary4 = 1500
eff_coef = 0.8

#Team2
#Developers
name8 = "Liam"
lastname8 = "Miller"
exper8 = 2
salary8 = 1000
name9 = "John"
lastname9 = "Wilson"
exper9 = 3
salary9 = 1100
name10 = "Harry"
lastname10 = "Moore"
exper10 = 4
salary10 = 1400
name11 = "Callum"
lastname11 = "Taylor"
exper11 = 5
salary11 = 1500
name12 = "Mason"
lastname12 = "Anderson"
exper12 = 6
salary12 = 1700
name13 = "Robert"
lastname13 = "Thomas"
exper13 = 7
salary13 = 1800
name14 = "Jacob"
lastname14 = "Jackson"
exper14 = 8
salary14 = 1900
name15 = "Michael"
lastname15 = "White"
exper15 = 9
salary15 = 2000

#Designers
name16 = "Kyle"
lastname16 = "Harris"
exper16 = 5
salary16 = 1500
eff_coef16 = 0.7
name17 = "Thomas"
lastname17 = "Martin"
exper17 = 6
salary17 = 1700
eff_coef17 = 0.9

#Manager for team2
name7 = "Joe"
lastname7 = "Thompson"
exper7 = 8
salary7 = 1500
team2 = []

#Managers
#CIO
name5 = "Connor"
lastname5 = "Davis"
exper5 = 5
salary5 = 2500

#Manager for team1
name6 = "Jake"
lastname6 = "Johnson"
exper6 = 4
salary6 = 1900
team1 = []

#employee1 = Employee(name1, lastname1, exper1, salary1)
#employee1.show()
developer1 = Developer(name1, lastname1, exper1, salary1, lastname6)
developer2 = Developer(name2, lastname2, exper2, salary2, lastname6)
developer3 = Developer(name3, lastname3, exper3, salary3, lastname6)

developer4 = Developer(name8, lastname8, exper8, salary8, lastname7)
developer5 = Developer(name9, lastname9, exper9, salary9, lastname7)
developer6 = Developer(name10, lastname10, exper10, salary10, lastname7)
developer7 = Developer(name11, lastname11, exper11, salary11, lastname7)
developer8 = Developer(name12, lastname12, exper12, salary12, lastname7)
developer9 = Developer(name13, lastname13, exper13, salary13, lastname7)
developer10 = Developer(name14, lastname14, exper14, salary14, lastname7)
developer11 = Developer(name15, lastname15, exper15, salary15, lastname7)



#developer1.show()
#developer2.show()
#developer3.show()
designer1 =  Designer(name4, lastname4, exper4, salary4, lastname6, eff_coef)

designer3 =  Designer(name16, lastname16, exper16, salary16, lastname16, eff_coef16)
designer4 =  Designer(name17, lastname17, exper17, salary17, lastname17, eff_coef17)

#designer1.show()
manager2 =  Manager(name6, lastname6, exper6, salary6, lastname5, team1)
manager3 =  Manager(name7, lastname7, exper7, salary7, lastname5, team2)
manager1 =  TopManager(name5, lastname5, exper5, salary5)

print(" ")
print("Our BOSS:")
manager1.show()
#manager2.show()

team_list1 = [developer1, developer2, developer3, designer1]
team1 = Team(team_list1)
print(" ")
print("Our Team 1:")
team1.show()

team_list2 = [developer4, developer5, developer6, developer7, developer8, developer9, developer10, developer11, designer3, designer4]
team2 = Team(team_list2)
print(" ")
print("Our Team 2:")
team2.show()

# list of managers with their own teams
manager_list = [manager2, manager3]
team_list_all = team_list1 + team_list2
department = Department(team_list_all, manager_list)

print(" ")
department.show()

print(" ")
print('Salary information (CIO not included): ')
department.salary_giving()

#	Oliver	Smith
#	Jake	Johnson
#	Noah	Williams
#	James	Jones
#	Jack	Brown
#	Connor	Davis
#	Liam	Miller
#	John	Wilson
#	Harry	Moore
#	Callum	Taylor
#	Mason	Anderson
#	Robert	Thomas
#	Jacob	Jackson
#	Michael	White
#	Kyle	Harris
#	Thomas	Martin
#	Joe	Thompson
#	Ethan	Garcia
#	David	Martinez
#	George	Robinson
#	Reece	Clark
#	Richard	Rodriguez
#	Oscar	Lewis
#	Rhys	Lee
#	Alexander	Walker
#	Joseph	Hall
#	Charlie	Allen
#	Charles	Young
#	William	Hernandez
#	Damian	King
#	Daniel	Wright
