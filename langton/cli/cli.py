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
@click.option("--debug", type=bool, is_flag=True)
def run(
    filepath: Path,
    iterations: int,
    fps: float,
    debug: bool = False,
) -> None:
    set_logging_config(debug)

    width = 140
    height = 140

    with Graphics.context(filepath=filepath, width=width, height=height, fps=fps) as graphics:
        rules = [
            Rule(current_color=Color.BLACK, turn=True, new_color=Color.WHITE),
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
