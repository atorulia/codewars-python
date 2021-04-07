def de_nico(key, message):
    """
    :param key: string consists of unique letters and digits
    :param message: string with encoded message
    :return: decoded message using the key.
    """
    key_length = len(key)
    order = [sorted(key).index(character) for character in key]
    split_message = [message[i:i+key_length] for i in range(0, len(message), key_length)]

    decoded_message = ""

    for part in split_message:
        for index in order:
            if index < len(part):
                decoded_message += part[index]

    return decoded_message.rstrip()

