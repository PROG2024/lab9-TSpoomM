"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    """
    Examples :
        >>> counter = Counter()
        >>> counter.count
        0
        >>> counter.count        # invoking count doesn't change anything
        0
        >>> counter.increment()  # add 1 and return the new count
        1

        >>> counter2 = Counter()
        >>> counter2 is counter
        True
        >>> counter2.count       # shares same count
        1
        >>> counter2.increment()  # add 1 and return the new count
        2
        >>> counter.count
        2
    """

    _instance = None

    # def __init__(self):
    #     self.__count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__count = 0
        return cls._instance

    def __str__(self):
        return f"{self.__count}"

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1
        return self.__count
