import lay
import data
import unittest
from unittest.mock import Mock

from unittest.mock import patch



class TestMethods(unittest.TestCase):

   
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

if __name__ == '__main__':
    unittest.main()