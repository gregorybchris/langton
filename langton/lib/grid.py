import logging
from typing import Tuple

import numpy as np

from langton.lib.color import Color

logger = logging.getLogger(__name__)


class Grid:
    shape: Tuple[int, int]
    data: np.ndarray

    def __init__(self, width: int, height: int):
        self.shape = width, height
        self.data = np.zeros((width, height), dtype=Color)
        self.data.fill(Color.BLACK)

    def get(self, x: int, y: int) -> Color:
        self.check_bounds(x, y)
        return self.data[x, y]

    def set(self, x: int, y: int, color: Color) -> None:
        self.check_bounds(x, y)
        self.data[x, y] = color

    def check_bounds(self, x: int, y: int) -> None:
        if x < 0 or x >= self.shape[0]:
            raise ValueError(f"x coordinate {x} out of bounds for width {self.shape[0]}")
        if y < 0 or y >= self.shape[1]:
            raise ValueError(f"y coordinate {y} out of bounds for height {self.shape[1]}")
