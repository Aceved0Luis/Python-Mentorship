from functools import reduce
from typing import Union
from typing import Tuple


def sum_numbers(number_1: Union[int, float], number_2: Union[int, float]) -> Union[int, float]:
    """
    Function that adds two numbers 
    entered as arguments and returns
    the result.
    """
    return number_1 + number_2

def multiply_numbers(*numbers: Tuple):
    """
    Function that multiplies a set of numbers
    passed as a tuple, because it will accept a 
    dynamic number of arguments.
    """
    return reduce(lambda number_1, number_2: number_1 * number_2, numbers)

def unpacking_arguments(a, b):
    """
    Function that will print two arguments.
    """
    print(a, b)


if __name__ == "__main__":
    # Calling the function `sum_numbers` and returning his value.
    result = sum_numbers(10, 12)
    print(result)

    # Calling the function `multiply_numbers`.
    print(multiply_numbers(4, 5))
    
    # Calling the function `multiply_number` with an undefined quantity of values.
    print(multiply_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    # Defining the arguments to be unpacked when the `unpacking_arguments` is going to be called.
    my_arguments = {
        "a": 1,
        "b": 2
    }

    unpacking_arguments(**my_arguments)

    # The previous statement is the same as the following statement ... 👇 
    unpacking_arguments(a=my_arguments['a'], b=my_arguments['b'])






