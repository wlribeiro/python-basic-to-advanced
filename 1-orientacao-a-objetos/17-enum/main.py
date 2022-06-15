from enum import Enum
from enum import auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError("cant move in this diction")

    return f"moveu para a {direction.name}"


if __name__ == "__main__" :
    print(move(Directions.right))
    print(move(Directions.right))
    print(move(Directions.left))