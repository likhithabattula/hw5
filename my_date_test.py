import unittest
import my_date


class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        # should return true, as given input is 1984
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        # should return false, as given input is 1985
        self.assertFalse(my_date.is_leap_year(1985))

    def test_ordinal_date1(self):
        # should return 1 when input given 1/1/2023
        self.assertEqual(my_date.ordinal_date(2023, 1, 1), 1)

    def test_ordinal_date2(self):
        #  should return 59 days when input is not a leap year and checking the date before feb 28th
        self.assertEqual(my_date.ordinal_date(2024, 2, 14), 45)

    def test_ordinal_date3(self):
        #  should return 61 days when input is a leap year and checking the date after March 1, 2024
        self.assertEqual(my_date.ordinal_date(2024, 3, 1), 61)

    def test_ordinal_date4(self):
        # should return ordinal days as 234, when given date is 08/22/1995(given date is my birthday :D)
        self.assertEqual(my_date.ordinal_date(1995, 8, 22), 234)


if __name__ == '__main__':
    unittest.main()
