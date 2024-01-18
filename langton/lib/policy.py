from dataclasses import dataclass
from typing import Dict, List, Self, Tuple

from langton.lib.color import Color
from langton.lib.turn import Turn
from langton.lib.update import Update

COLOR_ORDER = [
    Color.BLACK,
    Color.RED,
    Color.SALMON,
    Color.LIME,
    Color.GREEN,
    Color.BLUE,
    Color.YELLOW,
    Color.TEAL,
    Color.VIOLET,
    Color.ORANGE,
    Color.NAVY,
    Color.PINK,
    Color.GREY,
    Color.WHITE,
    Color.PEACH,
]


@dataclass
class Policy:
    update_map: Dict[Color, Update]

    @classmethod
    def from_str(cls, policy_str: str) -> Self:
        turns = []
        for s in policy_str:
            if s == "L":
                turns.append(Turn.LEFT)
            elif s == "R":
                turns.append(Turn.RIGHT)
            elif s == " ":
                continue
            else:
                raise ValueError(f"Invalid policy string, found {s}")

        if len(turns) > len(COLOR_ORDER):
            raise ValueError(f"Cannot create policy with {len(turns)} rules, max is {len(COLOR_ORDER)}")

        colors = COLOR_ORDER[: len(policy_str)]
        return cls.new(list(zip(colors, turns)))

    @classmethod
    def new(cls, sequence: List[Tuple[Color, Turn]]) -> Self:
        update_map = {}
        for i, _ in enumerate(sequence):
            j = (i + 1) % len(sequence)
            curr_color = sequence[i][0]
            turn = sequence[i][1]
            next_color = sequence[j][0]
            update_map[curr_color] = Update(turn, next_color)
        return cls(update_map)

    def get_update(self, color: Color) -> Update:
        if color not in self.update_map:
            raise ValueError(f"Could not find update for color {color}")

        return self.update_map[color]
