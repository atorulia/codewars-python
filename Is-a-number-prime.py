from math import sqrt
from itertools import count, islice


def is_prime(n: int) -> bool:
    """
    :param n: integer input, we can not assume that the integer will be only positive. We may be given negative numbers
    as well (or 0).
    :return: logical value true or false depending on if the integer is a prime
    """
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

