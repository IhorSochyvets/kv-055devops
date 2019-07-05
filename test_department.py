import unittest
from myPackage.Employee import Employee
from myPackage.Developer import Developer
from myPackage.Designer import Designer
from myPackage.Manager import Manager
from myPackage.TopManager import TopManager
from myPackage.Team import Team
from myPackage.Department import Department

class TestDepartment(unittest.TestCase):

#    def test_show(self):
#        #Assume
#        #Action
#        #Assert
#        department = Department([],[])
#        res = department.test_test()
#        self.assertEqual(res,2)

    def test_cheking_if_more_dev_then_des(self):
#        developer1 = Developer("Oliver", "Smith", 2, 1000, "Johnson")
#        developer2 = Developer("Noah", "Williams", 3, 1200, "Johnson")
#        developer3 = Developer("James", "Jones", 4, 1400, "Johnson")
#        designer1 =  Designer("Jack", "Brown", 4, 1500, "Johnson", 0.8)
#        manager2 =  Manager("Jake", "Johnson", 4, 1900, "Davis", [])
#        manager1 =  TopManager("Connor", "Davis", 5, 2500)
#        team_list1 = [developer1, developer2, developer3, designer1]
#       team1 = Team(team_list1)
#        manager_list = [manager2]
        department = Department(self.team_list1, self.manager_list)

        self.assertTrue(department.more_dev_then_des(),'message from testing 2 ')

    def test_cheking_salary_for_manager(self):

#        developer1 = Developer("Oliver", "Smith", 2, 1000, "Johnson")
#        developer2 = Developer("Noah", "Williams", 3, 1200, "Johnson")
#        developer3 = Developer("James", "Jones", 4, 1400, "Johnson")
#        designer1 =  Designer("Jack", "Brown", 4, 1500, "Johnson", 0.8)
#        manager2 =  Manager("Jake", "Johnson", 4, 1900, "Davis", [])
#        manager1 =  TopManager("Connor", "Davis", 5, 2500)
#        team_list1 = [developer1, developer2, developer3, designer1]
#       team1 = Team(team_list1)
#        manager_list = [manager2]
        department = Department(self.team_list1, self.manager_list)
        department.salary_giving2()

        self.assertEqual(self.manager2.salaryValue,2290.0)

    @classmethod
    def setUpClass(cls):
        cls.developer1 = Developer("Oliver", "Smith", 2, 1000, "Johnson")
        cls.developer2 = Developer("Noah", "Williams", 3, 1200, "Johnson")
        cls.developer3 = Developer("James", "Jones", 4, 1400, "Johnson")
        cls.designer1 =  Designer("Jack", "Brown", 4, 1500, "Johnson", 0.8)
        cls.manager2 =  Manager("Jake", "Johnson", 4, 1900, "Davis", [])
        cls.manager1 =  TopManager("Connor", "Davis", 5, 2500)
        cls.team_list1 = [cls.developer1, cls.developer2, cls.developer3, cls.designer1]
        cls.team1 = Team(cls.team_list1)
        cls.manager_list = [cls.manager2]
        print("before class")

    def tearDown(self):
        print("after test")

    def setUp(self):
        print("setup before each")

    @classmethod
    def tearDownClass(cls):
        print("after class")


if __name__ == '__main__':
    unittest.main()
