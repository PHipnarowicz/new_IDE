import unittest

from gender import gender_selector


class MyTestCase(unittest.TestCase):
    def test_female_gender_selector(self):
        self.assertEqual(gender_selector("Anna"), "F")
        self.assertEqual(gender_selector("Beata"), "F")

    def test_male_gender_selector(self):
        self.assertEqual(gender_selector("Piotr"), "M")
        self.assertNotEqual(gender_selector("Cecylia"), "M")

    def test_unknown_gender_selector(self):
        self.assertEqual(gender_selector(""), "unknown")
        self.assertEqual(gender_selector("Zuzia"), "unknown")
        self.assertEqual(gender_selector(111), "unknown")


if __name__ == '__main__':
    unittest.main()
