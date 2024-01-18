import logging
from pathlib import Path

import click

from langton.lib.graphics import Graphics
from langton.lib.policy import Policy
from langton.lib.simulation import Simulation

logger = logging.getLogger(__name__)


def set_logging_config(debug: bool) -> None:
    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format="%(message)s")


@click.group()
def main() -> None:
    """Main CLI entrypoint."""


@main.command()
@click.argument("filepath", type=Path)
@click.option("--iter", "iterations", type=int, default=1000)
@click.option("--fps", type=float, default=40.0)
@click.option("--width", type=int, default=100)
@click.option("--height", type=int, default=100)
@click.option("--debug", type=bool, is_flag=True)
def run(
    filepath: Path,
    iterations: int,
    fps: float,
    width: int,
    height: int,
    debug: bool = False,
) -> None:
    set_logging_config(debug)

    with Graphics.context(filepath=filepath, width=width, height=height, fps=fps) as graphics:
        policy = Policy.from_str("L R L L R L L L R R R L R L")

        with Simulation.context(
            graphics=graphics,
            iterations=iterations,
            width=width,
            height=height,
        ) as simulation:
            print(f"Running simulation for {iterations} iterations")
            simulation.run(policy)

        print(f"Saved to {filepath}")
