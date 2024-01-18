import logging
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Self, Tuple

import numpy as np

from langton.lib.color import Color
from langton.lib.cv import VideoWriter, codec_from_code

logger = logging.getLogger(__name__)


@dataclass
class Graphics:
    DEFAULT_SQUARE_SIZE = 10
    DEFAULT_FPS = 20.0

    shape: Tuple[int, int]
    buffer: np.ndarray
    video_writer: VideoWriter
    square_size: int = DEFAULT_SQUARE_SIZE
    fps: float = DEFAULT_FPS

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

        self.video_writer.write(self.buffer)

    @classmethod
    @contextmanager
    def context(
        cls,
        *,
        filepath: Path,
        width: int,
        height: int,
        square_size: int = DEFAULT_SQUARE_SIZE,
        fps: float = DEFAULT_FPS,
    ) -> Iterator[Self]:
        shape = width, height

        buffer = np.zeros((width * square_size, height * square_size, 3), dtype=np.uint8)
        video_writer = VideoWriter(
            str(filepath),
            codec_from_code("mp4v"),
            fps,
            (buffer.shape[1], buffer.shape[0]),
            True,
        )
        yield cls(
            shape=shape,
            buffer=buffer,
            video_writer=video_writer,
            square_size=square_size,
            fps=fps,
        )
        video_writer.release()
