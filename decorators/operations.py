from random import randint
from typing import Callable

"""
Now I want the `sum_numbers` function to add an extra random number 
to the operation in a range from 1 to 10.
"""

def add_extra_number(main_function: Callable) -> Callable:
    def inner_function(number1: int, number2: int, number3: int) -> int:
        result = main_function(number1, number2, number3)
        return result + randint(1, 10)
    return inner_function


@add_extra_number
def sum_numbers(n1, n2, n3):
    return n1 + n2 + n3

if __name__ == "__main__":
    """
    The statement that calls the `sum_numbers` function is
    modified internally by Python with a statement a like this ... 👇

    `print(add_extra_number(sum_numbers)(1, 2, 3))`
    """
    print(sum_numbers(1, 2, 3))