from typing import List


def likes(names: List[str]) -> str:
    """
    :param names: input array, containing the names of people who like an item.
    :return: display text as shown in the examples.
    """
    _likes = ""
    if len(names) > 3:
        _likes = str(names[0]) + ", " + str(names[1]) + " and " + str(int(len(names) - 2)) + " others like this"
    elif len(names) > 2:
        _likes = str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
    elif len(names) > 1:
        _likes = str(names[0]) + " and " + str(names[1]) + " like this"
    elif len(names) > 0:
        _likes = str(names[0]) + " likes this"
    else:
        _likes = "no one likes this"
    return _likes

