class SecureList:
    """
    The White House is currently developing a mobile app that it can use to issue instructions to its undercover agents.
    Part of the functionality of this app is to have messages that can be read only once, and are then destroyed.
    """
    def __init__(self, base: list):
        """
        Initialize SecureList class
        :param base: list item with any content
        """
        self._base = [item for item in base]

    def __getitem__(self, item: int):
        """
        :param item: position of item for pop from list
        :return: popped item
        """
        return self._base.pop(item)

    def __str__(self):
        """
        :return: string value of list items (base list will be cleared after return)
        """
        str_line = str(self._base)
        self._base.clear()
        return str_line

    def __repr__(self):
        """
        :return: string value of list items (base list will be cleared after return)
        """
        repr_line = str(self._base)
        self._base.clear()
        return repr_line

    def __len__(self):
        """
        :return: length of base list
        """
        return len(self._base)
