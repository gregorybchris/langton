from dataclasses import dataclass

from langton.lib.color import Color
from langton.lib.turn import Turn


@dataclass
class Rule:
    current_color: Color
    turn: Turn
    new_color: Color
