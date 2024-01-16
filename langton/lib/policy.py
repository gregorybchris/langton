from dataclasses import dataclass
from typing import List

from langton.lib.rule import Rule


@dataclass
class Policy:
    rules: List[Rule]
