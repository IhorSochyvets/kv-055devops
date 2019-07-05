import unittest
from myPackage.math_example import myFun


class MyFunTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(myFun(self.myinput), 4)

    def test_negative(self):
        with self.assertRaises(TypeError):
            myFun(self.myfailinput)

    def test_failed(self):
        self.assertEqual(myFun("2"), 4)

    @classmethod
    def setUpClass(cls):
        cls.myinput = 2
        cls.myfailinput = "a"
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
