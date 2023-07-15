def even_number_of_evens(numbers):
    """
    Goal: Check how many even numbers are there in a list of evens
    Test:
        - TypeError if list not paseed
        - if 'numbers' is empty return False
        - Number is odd return False
        - Number is 0 return False
        - Number is even return True
    """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])  # List Comprehension
        print(f'There are "{evens} evens" in the list')
        return True if evens and evens % 2 == 0 else False  # 1-line "if/else"
    else:
        raise TypeError(f'{numbers} is not a list!')


numbers = [2, 5, 6, 8, 10]

if __name__ == '__main__':
    print(even_number_of_evens(numbers))
