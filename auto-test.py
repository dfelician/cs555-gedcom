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
        self.assertEqual(len(albert.isBirthBeforeMarriage()), 3)

    def testBirthBeforeMarriage2(self):
        self.assertEqual(albert.isBirthBeforeMarriage(), [
        'Anomoly US08: Birth date of Courtney /Reynolds/(I12) occurs before the marriage date of his parents in Family (F4)', 
        'Anomoly US08: Birth date of Travis /Frick/(I14) occurs over 9 months after the divorce date of his parents in Family (F6)',
        'Anomoly US08: Birth date of Kelly /Frick/(I15) occurs over 9 months after the divorce date of his parents in Family (F6)'
        ])

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
    
    def test_US27isInt(self):
        people = data.personData()
        for person in people:
            self.assertTrue(type(person.age), int)

    def test_US31correctPerson(self):
        singlePeople = david.getLivingSingle()
        self.assertEqual(singlePeople[0].name, "Courtney /Reynolds/")
    
    def test_US36lessThan30Days(self):
        self.assertTrue(david.diedWithin30Days(date(2022, 10, 10)))
    
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
    
    def test_numberOfDivorceError(self):
        divorceStrings = bhavin.divorceBeforeDeath()
        self.assertEqual(len(divorceStrings), 0)

    def test_typeOfDivorceError(self):
        self.assertEqual(type(bhavin.divorceBeforeDeath()), list)

    def test_numberOfMarriageError(self):
        marriageStrings = bhavin.marriageBeforeDeath()
        self.assertEqual(len(marriageStrings), 0)

    def test_typeOfMarriageError(self):
        self.assertEqual(type(bhavin.marriageBeforeDeath()), list)

    def test_numberOfUniqueIdError(self):
        uniqueIdStrings = bhavin.isIdUnique()
        self.assertEqual(len(uniqueIdStrings), 0)
    
    def test_typeOfUniqueIdError(self):
        self.assertEqual(type(bhavin.isIdUnique()), list)

    #Bhavin - End
    


    #Lay
    def test1_isDateValid(self):
        self.assertEqual(len(lay.isDateValid()), 1)

    def test2_isDateValid(self):
        self.assertEqual(lay.isDateValid()[0], "Error: INDIVIDUAL: US01: I8: Birthday 2050-04-06 occurs in the future")

    def test3_isDateValid(self):
        self.assertEqual(type(lay.isDateValid()), list)

    def test4_isDateValid(self):
        self.assertEqual(lay.isDateValid()[0], "Error: INDIVIDUAL: US01: I8: Birthday 2050-04-06 occurs in the future")

    def test5_isDateValid(self):
        self.assertIn("Error: INDIVIDUAL: US01: I8: Birthday 2050-04-06 occurs in the future" ,lay.isDateValid())
    
    #Lay - End



if __name__ == '__main__':
    unittest.main()