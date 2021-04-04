import re


class Mod:
    """
    Given number is multiple by 4 if:
    - the module gives 0
    - if the tens digit is even and the last digit is 0, 4 or 8
    - if the tens digit is uneven and last digit is 2 or 6
    - if it's zero
    - if one nonzero digit is 4 or 8
    """
    mod4 = re.compile(r"(.)*\[[+-]?0*(\d*(([02468][048])|([13579][26]))|([048]))].*")
