import unittest

from gender import gender_selector


class MyTestCase(unittest.TestCase):
    def test_gender_selector(self):
        self.assertEqual(gender_selector("Anna"), "F")


if __name__ == '__main__':
    unittest.main()
