from typing import List


def create_phone_number(n: List[int]) -> str:
    """
    :param n: array of 10 integers (between 0 and 9)
    :return: string of numbers in the form of a phone number
    """
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
