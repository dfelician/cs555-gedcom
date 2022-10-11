import albert
import unittest

class TestMethods(unittest.TestCase):
    def testMarriedBeforeDivorce(self):
        self.assertEqual(len(albert.isBirthBeforeMarriage()), 2)

    #def testMarriedBeforeDivorce(self):
        #self.assertEqual(len(albert.isBirthBeforeMarriage()), 1)

if __name__ == '__main__':
    unittest.main()