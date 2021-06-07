"""Main functions for Codemelli."""

from json import load
from os import path
from random import randint, choice
from re import search
from typing import Union


def city_codes_data() -> dict:
    """Return a dict containing city codes.

    :return: city codes
    :rtype: dict
    """
    with open(f'{path.dirname(path.realpath(__file__))}/data/code-city.json',
              'r', encoding='utf-8') as json_file:
        return load(json_file)  # get data from json file


def validator(input_code: int, strict: bool = False) -> bool:
    """Validate the input code by CodeMelli rules.

    :param int input_code: a CodeMelli number
    :param bool strict: Checks validation of city code
    :return: validation result
    :rtype: bool

    :raises ValueError: if input code is not a 10-digit number
    :raises ValueError: if input code does not start with a valid city code
    """
    # integer to string type conversion, input should be iterable
    input_code = str(input_code)

    # check if the input is formatted correctly
    if not search(r'^\d{10}$', input_code):
        raise ValueError('input code should be a 10-digit number')

    # check if input code does not start with a valid city code
    if strict is True and lookup(input_code) is None:
        raise ValueError(
            f'input code started with an invalid city code: {input_code[:3]}'
        )

    # select the last character of input code.
    # it will be used for validating other characters
    checker = int(input_code[-1])

    # convert out input code (str) to a list[int]
    input_list_int = [int(i) for i in input_code[:-1]]

    # calculate the remainder of CodeMelli formula
    remainder = _get_remainder(input_list_int)

    # return True if conditions are passed. In contrast, return False
    return (2 > remainder == checker) or \
           (remainder >= 2 and checker + remainder == 11)


def generator(city_code: str = None) -> str:
    """Generate a random valid CodeMelli.

    :param str city_code: An string of numbers (length=3)
    :return: A valid CodeMelli
    :rtype: str

    :raises ValueError: if city code is defined and it is not 3-digit number
    """
    # Get a random city code from json file if it is not defined by the user
    if city_code is None:
        data = city_codes_data()
        city_code = choice(list(data.keys()))

    # Convert city code to string
    city_code = str(city_code)

    # Raise a value error if the city code does not contain 3 numbers
    if not search(r'^\d{3}$', city_code):
        raise ValueError(f'City code should be an integer of length 3.'
                         f'"{city_code}" is not a valid value')

    # Convert city code to a list of integers
    city_code = list(map(int, city_code))

    # Generate 6 random integers for rest of the codeMelli
    random_codemelli = city_code + [randint(0, 9) for i in range(6)]

    # get remainder of generate codeMelli
    remainder = _get_remainder(random_codemelli)

    # calculating the last number of the generated codeMelli
    last_num = remainder if (remainder < 2) else 11 - remainder

    # put it all together and return
    return "".join([str(x) for x in random_codemelli + [last_num]])


def lookup(input_code: str) -> dict or None:
    """Lookup state and city of the input code.

    :param str input_code: a CodeMelli string
    :return: state and city of the given CodeMelli in the following format:
        {state: example_state,
        city: example_city}
    :rtype: dict or None
    """
    # force convert input_code to string
    input_code = str(input_code)

    # select first 3 characters of input code
    prefix = input_code[:3]
    data = city_codes_data()

    # return a dict if the first 3 characters exist in our data
    if prefix in data.keys():
        return data[prefix]

    return None


def _get_remainder(code: Union[list, int]) -> int:
    """Calculate remainder of validation calculations.

    :param Union[list, int] code: input code
    :return: remainder of calculations
    :rtype: int

    :raises TypeError: if code is not a list or an integer
    """
    # raise an exception if code is not a list or an integer
    if not isinstance(code, (list, int)):
        raise TypeError('code should be a list or an integer')

    # convert integer code to a list of integers
    if isinstance(code, int):
        code = list(map(int, str(code)))

    # a 10 to 2 list, it will be used for next calculation
    reversed_range = range(10, 1, -1)

    # calculate the remainder of CodeMelli formula division
    return sum([i * j for i, j in zip(code, reversed_range)]) % 11


if __name__ == "__main__":
    # Generate a random codemelli
    print(generator())
