from typing import List


def max_sequence(arr: List[int]) -> int:
    """The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or
    list of integers
    :param arr: list of integers
    :return: max sum of subarray
    """
    return max([sum(arr[i:j]) for i in range(len(arr) + 1) for j in range(i, len(arr) + 1)]) if len(arr) else 0
