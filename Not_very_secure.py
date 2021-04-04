import re


def alphanumeric(password):
    if re.match(r'^[a-zA-Z\d]+$', password):
        return True

    return False


print(alphanumeric(input()))