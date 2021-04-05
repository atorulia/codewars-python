from typing import Optional


def extract_number(word: str) -> Optional[int]:
    """
    Let's say that there is only one digit in a word, this function looks for this digit
    :param word: word for working with
    :return: digit which found or None
    """
    for letter in word:
        if letter.isdigit():
            return int(letter)
    return None


def order(sentence: str) -> str:
    """
    :param sentence: line with words that contains one digit as sorting key
    :return: sorted line
    """
    return ' '.join(sorted(sentence.split(), key=extract_number))
