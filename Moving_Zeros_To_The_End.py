def move_zeros(array: list) -> list:
    """
    :param array: list with any content
    :return: return that array but with zeros in the end
    """
    items = [_ for _ in array if isinstance(_, bool) or _ != 0]
    return items + [0 for _ in range(0, len(array) - len(items))]
