# import unittest
# from evens import even_number_of_evens


# class TestEvens(unittest.TestCase):  # Test Case

#     def test_return_true(self):
#         self.assertTrue(even_number_of_evens([]))


# if __name__ == '__main__':
#     unittest.main()

#########################

# def even_number_of_evens(numbers):
#     """
#     Even number of evens:
#     - TypeError if list not paseed
#     - if 'numbers' is empty return False
#     - Number is odd return False
#     - Number is 0 return False
#     - Number is even return True
#     """
#     if isinstance(numbers, list):
#         if numbers == []:
#             print(f'{numbers}: is an empty list!')
#             return True
#         else:
#             evens = 0

#         for n in numbers:
#             if n % 2 == 0:
#                 evens += 1

#         if evens:
#             evens % 2 == 0
#             print(f'Great: "{evens}" is an Even number!')
#             return True
#         else:
#             print(f'{evens}: is an Odd or 0 number!')
#             return False
#     else:
#         raise TypeError(f'{numbers} is not a list!')


# numbers = [2, 4, 6, 8, 10]

# if __name__ == '__main__':
#     print(even_number_of_evens(numbers))
