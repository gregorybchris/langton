from enum import StrEnum, auto
from typing import Tuple


class Color(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    CYAN = auto()
    MAGENTA = auto()
    WHITE = auto()
    BLACK = auto()

    def to_rgb(self) -> Tuple[int, int, int]:
        return {
            Color.RED: (255, 0, 0),
            Color.GREEN: (0, 255, 0),
            Color.BLUE: (0, 0, 255),
            Color.YELLOW: (255, 255, 0),
            Color.CYAN: (0, 255, 255),
            Color.MAGENTA: (255, 0, 255),
            Color.WHITE: (255, 255, 255),
            Color.BLACK: (0, 0, 0),
        }[self]
