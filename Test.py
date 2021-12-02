import unittest
from main import PhoneBook

class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEqual(PhoneBook.getContactByName(["A-79345657"], "A"), "79345657")
        self.assertEqual(PhoneBook.getContactByName(["B-7898403"], "B"), "7898403")


if __name__ == '__main__':
    unittest.main()
