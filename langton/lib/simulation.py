from contextlib import contextmanager
from dataclasses import dataclass
from typing import Iterator, Self, Tuple

from tqdm import tqdm

from langton.lib.graphics import Graphics
from langton.lib.grid import Grid
from langton.lib.policy import Policy
from langton.lib.turn import Turn


@dataclass
class Simulation:
    DEFAULT_NTH_FRAME = 1

    graphics: Graphics
    iterations: int
    grid: Grid
    nth_frame: int

    def run(self, policy: Policy) -> None:
        x = self.grid.shape[0] // 2
        y = self.grid.shape[1] // 2
        dx = 1
        dy = 0
        for i in tqdm(range(self.iterations)):
            current_color = self.grid.get(x, y)
            update = policy.get_update(current_color)
            write_frame = i % self.nth_frame == 0
            self.graphics.draw(x, y, color=current_color, write_frame=write_frame)
            self.grid.set(x, y, color=update.color)
            dx, dy = self.make_turn(dx, dy, update.turn)
            x += dx
            y += dy

    def make_turn(self, dx: int, dy: int, turn: Turn) -> Tuple[int, int]:
        if turn == Turn.RIGHT:
            return dy, -dx
        return -dy, dx

    @classmethod
    @contextmanager
    def context(
        cls,
        *,
        graphics: Graphics,
        iterations: int,
        width: int,
        height: int,
        nth_frame: int = DEFAULT_NTH_FRAME,
    ) -> Iterator[Self]:
        grid = Grid(width, height)
        yield cls(
            graphics=graphics,
            iterations=iterations,
            grid=grid,
            nth_frame=nth_frame,
        )
