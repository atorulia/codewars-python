def narcissistic(value: int) -> bool:
    """
    :param value: number for checking
    :return: bool value depending upon whether the given number is a Narcissistic number in base
    """
    return sum(int(i)**len(str(value)) for i in str(value)) % value == 0
