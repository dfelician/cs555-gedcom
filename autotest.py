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
        self.assertEqual(len(albert.isBirthBeforeMarriage()), 20)

    def testBirthBeforeMarriage2(self):
        self.assertIn("Anomoly US08: Birth date of Thomas /Drake/(I37) occurs before the marriage date of his parents in Family (F11)", albert.isBirthBeforeMarriage())

    def testBirthBeforeMarriage3(self):
        self.assertEqual(type(albert.isBirthBeforeMarriage()), list)
    
    def testBirthBeforeMarriage4(self):
        if (len(albert.isBirthBeforeMarriage()) > 0):
             self.assertEqual(type(albert.isBirthBeforeMarriage()[0]), str)

    def testBirthBeforeMarriage5(self):
        for msg in albert.isBirthBeforeMarriage():
            self.assertIsNot(msg, "")

    def testIsMarriedBeforeDivorce(self):
        self.assertEqual(len(albert.isMarriedBeforeDivorce()), 1)

    def testIsBirthBeforeParentsDeath(self):
        self.assertIn("Error: FAMILY: US09: Birth date of Brian /Frick/(I10) occurs more than 9 months after the death date of father (I1)", albert.isBirthBeforeParentsDeath())

    def testIsSibilingSpacing(self):
        self.assertIn("Error: FAMILY: US13: Birth date of Angelica /Drake/(I40) is less than 8 months and more than 2 days apart from Jessica /Drake/(Jessica /Drake/)", albert.isSibilingSpacing())

    def testNonDescendentMarriage(self):
        self.assertIn("Error: FAMILY: US17: Spouse cannot be a descendent of the family.", albert.nonDescendentMarriage())

    def testIsUniqueFamilyBySpouse(self):
        self.assertIn("Error: FAMILY: US24: Spouse I10 can not be in multiple families with the same marriage date.", albert.isUniqueFamilyBySpouse())
    #Albert - End



    #David
    def test_lessThan30Days(self):
        self.assertTrue(david.isWithin30Days(date(2022, 10, 30)))

    def test_moreThan30Days(self):
        self.assertFalse(david.isWithin30Days(date(2020, 10, 10)))

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
        self.assertTrue(david.isWithin30Days(date(2022, 10, 10)))

    def test_US07lessThan150(self):
        lessThen150Strings = david.lessThen150()
        self.assertIn("Error: INDIVIDUAL: US07: I24 Elena /Francis/ birth is 150 years or more before today", lessThen150Strings)

    def test_US27orderSiblingsByAge(self):
        orderedSiblingsKey = list(david.orderSiblingsByAge())[0]
        self.assertEqual("F1", orderedSiblingsKey)
    #David - End
    


    #Bhavin
    def test_oneDeath(self):
        self.assertEqual(len(bhavin.getDeaths()), 3, "should be 3 death")

    def test_nameOfDeceased(self):
        self.assertEqual(bhavin.getDeaths()[0].name, "Paul /Frick/", "Paul /Frick/")
        
    def test_checkIfNameExists(self):
        deaths = bhavin.getDeaths()
        # for person in deaths:
        self.assertIn("Paul", deaths[0].name)

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
        self.assertIn("Error: FAMILY: US06: Divorce occurs after death of spouse I31 Death Date 2004-07-15 Divorce Date: 2009-10-07", divorceStrings)

    def test_numberOfMarriageError(self):
        marriageStrings = bhavin.marriageBeforeDeath()
        self.assertIn("Error: FAMILY: US05: Marriage occurs after death of spouse I32 Death Date 1968-01-27 Marriage Date: 1969-12-15", marriageStrings)

    def test_numberOfUniqueIdError(self):
        uniqueIdStrings = bhavin.isIdUnique()
        self.assertIn("Error: INDIVIDUAL: US22: I32 is not a unique ID", uniqueIdStrings)

    def test_US15_lessThan15Siblings(self):
        siblingStrings = bhavin.lessThan15Siblings()
        self.assertIn("Error: FAMILY: US15: There are 15 or more siblings in family F11", siblingStrings)

    def test_US18_siblingsShouldNotMarry(self):
        siblingsMarriedStrings = bhavin.siblingsShouldNotMarry()
        self.assertIn("Error: FAMILY: US18: Siblings should not marry each other F11", siblingsMarriedStrings)

    #Bhavin - End
    


    #Lay
    def test_US1_isDateValid(self):
        self.assertEqual(len(lay.isDateValid()), 1)

    def test_US1_test2_isDateValid(self):
        self.assertEqual(lay.isDateValid()[0], "Error: INDIVIDUAL: US01: I10: Birthday 2050-04-06 occurs in the future")

    def test_US_1test3_isDateValid(self):
        self.assertEqual(type(lay.isDateValid()), list)

    def test_US1_test4_isDateValid(self):
        self.assertEqual(lay.isDateValid()[0], "Error: INDIVIDUAL: US01: I10: Birthday 2050-04-06 occurs in the future")

    def test_US1_test5_isDateValid(self):
        self.assertIn("Error: INDIVIDUAL: US01: I10: Birthday 2050-04-06 occurs in the future" ,lay.isDateValid())
    
    def test_US10_marriageAfter14(self):
        self.assertIn("Error: FAMILY: US10: F8: Husband Birthdate 2050-04-06 is less than 14 years of Marriage Date 2009-05-07", lay.isMarriageAfter14())

    def test_US12_parentsOld(self):
        self.assertIn("Error: FAMILY: US12: F2 Mother is greater than 60 years old, Mother id: I2", lay.isParentsOld())

    def test_US14_multipleBirths(self):
        self.assertIn("Error: FAMILY: US14: F11 More than 5 siblings are born at the same time", lay.multipleBirths())

    def test_US16_sameLastNameMale(self):
        self.assertIn("Error: FAMILY: US16: F11 Not all male members of the family have the same last name of Wigley", lay.sameLastNameMale())
    
    def test_US21_correctGenderRole(self):
        self.assertNotIn("Error: FAMILY: US21: Family Husband is not gender Male, Husband id: I23", lay.correctGenderRole())
    
    def test_US23_uniqueNameBirth(self):
        self.assertIn("Error: INDIVIDUAL: US23: More than 1 individuals with same name and birthdays Francis /Drake/2022-01-01", lay.uniqueNameBirth())
    
    def test_US25_uniqueFirstNameInFamily(self):
        self.assertIn("Error: FAMILY: US25: More than 1 children with same name and birthday, family id F11 with children Francis /Drake/2022-01-01", lay.uniqueFirstNameInFamily())
    #Lay - End



if __name__ == '__main__':
    unittest.main()