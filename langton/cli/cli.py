import logging
from pathlib import Path

import click

from langton.lib.color import Color
from langton.lib.graphics import Graphics
from langton.lib.policy import Policy
from langton.lib.rule import Rule
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
        rules = [
            Rule(current_color=Color.BLACK, turn=False, new_color=Color.RED),
            Rule(current_color=Color.RED, turn=False, new_color=Color.BLUE),
            Rule(current_color=Color.BLUE, turn=False, new_color=Color.YELLOW),
            Rule(current_color=Color.YELLOW, turn=True, new_color=Color.GREEN),
            Rule(current_color=Color.GREEN, turn=False, new_color=Color.YELLOW),
            Rule(current_color=Color.YELLOW, turn=True, new_color=Color.VIOLET),
            Rule(current_color=Color.VIOLET, turn=True, new_color=Color.TEAL),
            Rule(current_color=Color.TEAL, turn=False, new_color=Color.ORANGE),
            Rule(current_color=Color.ORANGE, turn=True, new_color=Color.WHITE),
            Rule(current_color=Color.WHITE, turn=False, new_color=Color.BLACK),
        ]
        policy = Policy(rules=rules)

        with Simulation.context(
            graphics=graphics,
            iterations=iterations,
            width=width,
            height=height,
        ) as simulation:
            print(f"Running simulation for {iterations} iterations")
            simulation.run(policy)

        print(f"Saved to {filepath}")
