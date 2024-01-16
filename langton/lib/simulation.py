from contextlib import contextmanager
from dataclasses import dataclass
from typing import Iterator, Self, Tuple

from langton.lib.graphics import Graphics
from langton.lib.grid import Grid
from langton.lib.policy import Policy


@dataclass
class Simulation:
    graphics: Graphics
    iterations: int
    grid: Grid

    def run(self, policy: Policy) -> None:
        x = self.grid.shape[0] // 2
        y = self.grid.shape[1] // 2
        dx = 1
        dy = 0
        for _ in range(self.iterations):
            for rule in policy.rules:
                current_color = self.grid.get(x, y)
                if current_color == rule.current_color:
                    self.graphics.draw(x, y, color=current_color)
                    self.grid.set(x, y, color=rule.new_color)
                    dx, dy = self.make_turn(dx, dy, rule.turn)
                    x += dx
                    y += dy
                    break
            self.graphics.save_frame()

    def make_turn(self, dx: int, dy: int, turn: bool) -> Tuple[int, int]:
        if turn:
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
    ) -> Iterator[Self]:
        grid = Grid(width, height)
        yield cls(
            graphics=graphics,
            iterations=iterations,
            grid=grid,
        )