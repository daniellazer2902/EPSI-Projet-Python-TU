import unittest

from main import CheckPasswordServiceTest


class TestAll(unittest.TestCase):

    def test_all(self):
        testSuite = unittest.TestSuite()
        testResult = unittest.TestResult()
        testSuite.addTest(unittest.makeSuite(CheckPasswordServiceTest))
        print(testResult.testsRun)


if __name__ == "__main__":
    unittest.main()