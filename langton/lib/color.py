from enum import StrEnum, auto
from typing import Tuple


class Color(StrEnum):
    LIME = auto()
    SALMON = auto()
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    TEAL = auto()
    VIOLET = auto()
    ORANGE = auto()
    NAVY = auto()
    PINK = auto()
    WHITE = auto()
    BLACK = auto()
    GREY = auto()
    PEACH = auto()

    def to_rgb(self) -> Tuple[int, int, int]:
        return {
            Color.LIME: (123, 237, 159),
            Color.SALMON: (249, 127, 81),
            Color.RED: (231, 76, 60),
            Color.GREEN: (46, 204, 113),
            Color.BLUE: (52, 152, 219),
            Color.YELLOW: (241, 196, 15),
            Color.TEAL: (26, 188, 156),
            Color.VIOLET: (155, 89, 182),
            Color.ORANGE: (230, 126, 34),
            Color.NAVY: (52, 73, 94),
            Color.PINK: (243, 104, 224),
            Color.WHITE: (236, 240, 241),
            Color.BLACK: (0, 0, 0),
            Color.GREY: (164, 176, 190),
            Color.PEACH: (230, 103, 103),
        }[self]
