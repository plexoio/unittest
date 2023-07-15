import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):  # Test Case

    def test_if_no_list_passed_throw_error(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_if_empty_list_passed(self):
        self.assertEqual(even_number_of_evens([]), False)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == "__main__":
    unittest.main()
