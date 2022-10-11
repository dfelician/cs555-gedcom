import albert
import unittest

class TestMethods(unittest.TestCase):
    def testBirthBeforeMarriage1(self):
        self.assertEqual(len(albert.isBirthBeforeMarriage()), 2)

    def testBirthBeforeMarriage2(self):
        self.assertEqual(albert.isBirthBeforeMarriage(), ['Anomoly US08: Birth date of Travis /Frick/(I14) occurs over 9 months after the divorce date of his parents in Family (F6)', 
        'Anomoly US08: Birth date of Kelly /Frick/(I15) occurs over 9 months after the divorce date of his parents in Family (F6)'])

    def testBirthBeforeMarriage3(self):
        self.assertEqual(type(albert.isBirthBeforeMarriage()), list)
    
    def testBirthBeforeMarriage4(self):
        if (len(albert.isBirthBeforeMarriage()) > 0):
             self.assertEqual(type(albert.isBirthBeforeMarriage()[0]), str)

    def testBirthBeforeMarriage5(self):
        for msg in albert.isBirthBeforeMarriage():
            self.assertIsNot(msg, "")

if __name__ == '__main__':
    unittest.main()