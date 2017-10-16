from calculator import Count
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

class TestAdd(unittest.TestCase):



    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j=Count(41,76)
        self.assertEqual(j.add(),117)




class TestSub(unittest.TestCase):

    def test_sub(self):
        j=Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j=Count(71,46)
        self.assertEqual(j.sub(),25)


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add2"))
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_sub2"))

    runner = unittest.TextTestRunner
    runner.run(suite)