import logging
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, List, Self, Tuple

import numpy as np
from PIL import Image

from langton.lib.color import Color

logger = logging.getLogger(__name__)


@dataclass
class Graphics:
    DEFAULT_SQUARE_SIZE = 10

    shape: Tuple[int, int]
    buffer: np.ndarray
    images: List[Image.Image] = field(default_factory=list)
    square_size: int = DEFAULT_SQUARE_SIZE

    def draw(self, x: int, y: int, color: Color) -> None:
        logger.debug(f"Drawing square at ({x}, {y}) with color {color}")

        if x < 0 or x >= self.shape[0]:
            logger.debug(f"x coordinate {x} out of bounds for width {self.shape[0]}")
            return
        if y < 0 or y >= self.shape[1]:
            logger.debug(f"y coordinate {y} out of bounds for height {self.shape[1]}")
            return

        for r in range(self.square_size):
            for c in range(self.square_size):
                rx = x * self.square_size + r
                cy = y * self.square_size + c
                self.buffer[rx, cy] = color.to_rgb()

    def save_frame(self) -> None:
        logger.debug("Saving image")
        image = Image.fromarray(self.buffer.astype(np.uint8), mode="RGB")
        self.images.append(image)

    def save_video(self, filepath: Path) -> None:
        logger.debug("Saving video")
        image = Image.new("RGB", self.buffer.shape[:2])
        image.save(filepath, save_all=True, append_images=self.images)

    @classmethod
    @contextmanager
    def context(cls, *, width: int, height: int, square_size: int = DEFAULT_SQUARE_SIZE) -> Iterator[Self]:
        shape = width, height
        buffer = np.zeros((width * square_size, height * square_size, 3), dtype=np.uint8)
        yield cls(shape=shape, buffer=buffer, square_size=square_size)
