from dataclasses import dataclass

from langton.lib.color import Color
from langton.lib.turn import Turn


@dataclass
class Update:
    turn: Turn
    color: Color
