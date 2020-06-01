from enum import Enum, unique

@unique
class Move(Enum):
    RAISE = 0
    LOWER = 1
    UPPER_LEFT = 2
    UPPER_RIGHT = 3
    LOWER_LEFT = 4
    LOWER_RIGHT = 5
    VOID = 6

    @staticmethod
    def next(current):
        return Move(current.value + 1)
