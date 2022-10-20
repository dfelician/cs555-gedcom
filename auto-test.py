import unittest
import data
from datetime import date

import albert
import bhavin
import david
import lay

class TestMethods(unittest.TestCase):
    #Albert
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

    #Albert - End



    #David
    def test_lessThan30Days(self):
        self.assertTrue(david.bornWithin30Days(date(2022, 9, 30)))

    def test_moreThan30Days(self):
        self.assertFalse(david.bornWithin30Days(date(2020, 10, 10)))

    def test_correctNumberOfRecentBirths(self):
        self.assertEqual(len(david.getRecentBirths()), 1)

    def test_correctPerson(self):
        self.assertEqual(david.getRecentBirths()[0].name, "Layla /Frick/")

    def test_correctObject(self):
        recentBirths = david.getRecentBirths()
        for person in recentBirths:
            self.assertEqual(type(person), data.Person)
    
    #David - End
    


    #Bhavin
    def test_oneDeath(self):
        self.assertEqual(len(bhavin.getDeaths()), 1, "should be 1 death")

    def test_nameOfDeceased(self):
        self.assertEqual(bhavin.getDeaths()[0].name, "Paul /Frick/", "Paul /Frick/")
        
    def test_checkIfNameExists(self):
        deaths = bhavin.getDeaths()
        for person in deaths:
            self.assertIn("Paul", person.name)

    def test_checkIfNameDoesNotExists(self):
        deaths = bhavin.getDeaths()
        for person in deaths:
            self.assertNotIn("David", person.name)

    def test_personsAreDeceased(self):
        deaths = bhavin.getDeaths()
        for person in deaths:
            self.assertFalse(person.alive, "Should be False")

    #Bhavin - End
    


    #Lay
    def test1_isDateValid(self):
        self.assertEqual(len(lay.isDateValid()), 3)

    def test2_isDateValid(self):
        self.assertEqual(lay.isDateValid()[0], "Error: INDIVIDUAL: US01: I1\n: Birthday 2025-05-05 occurs in the future")

    def test3_isDateValid(self):
        self.assertEqual(type(lay.isDateValid()), list)

    def test4_isDateValid(self):
        self.assertEqual(lay.isDateValid()[1], "Error: INDIVIDUAL: US01: I3\n: Birthday 3000-02-07 occurs in the future")

    def test5_isDateValid(self):
        self.assertIn("Error: INDIVIDUAL: US01: I8\n: Birthday 2050-04-06 occurs in the future" ,lay.isDateValid())
    
    #Lay - End



if __name__ == '__main__':
    unittest.main()