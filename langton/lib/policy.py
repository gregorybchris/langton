from dataclasses import dataclass
from typing import Dict, List, Self

from langton.lib.color import Color
from langton.lib.update import Update


@dataclass
class Policy:
    update_map: Dict[Color, Update]

    @classmethod
    def new(cls, sequence: List) -> Self:
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
