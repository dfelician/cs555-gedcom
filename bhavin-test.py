import bhavin
import unittest

class TestStringMethods(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main() 