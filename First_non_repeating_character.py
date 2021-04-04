def first_non_repeating_letter(string: str) -> str:
    """
    :param string: string input
    :return: first character that is not repeated anywhere in the string.
    """
    for character in string:
        if not string.lower().count(character.lower()) > 1:
            return character

    return ''
