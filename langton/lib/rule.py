from dataclasses import dataclass

from langton.lib.color import Color


@dataclass
class Rule:
    current_color: Color
    turn: bool
    new_color: Color
