import unittest
from datetime import date
import david
import data


class TestUS35(unittest.TestCase):
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


class TestUS27(unittest.TestCase):
    def test_isInt(self):
        people = data.personData()
        for person in people:
            self.assertTrue(type(person.age), int)


class TestUS31(unittest.TestCase):
    def test_correctPerson(self):
        singlePeople = david.getLivingSingle()
        self.assertEqual(singlePeople[0].name, "Dillon /Reynolds/")


class TestUS36(unittest.TestCase):
    def test_lessThan30Days(self):
        self.assertTrue(david.diedWithin30Days(date(2022, 10, 10)))


if __name__ == '__main__':
    unittest.main()
    