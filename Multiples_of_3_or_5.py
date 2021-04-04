def solution(number: int) -> int:
    """
    :param number: number for listing natural numbers between 0 and number
    :return: sum of numbers that are multiples of 3 or 5
    """
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
