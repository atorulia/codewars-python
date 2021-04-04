def square_digits(num: int):
    """
    :param num: number for taking square of digits
    :return: concatenate squares of digits
    """
    return int(''.join(str(e) for e in [i**2 for i in list(map(int, str(num)))]))

