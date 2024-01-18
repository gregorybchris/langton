import logging
from pathlib import Path
from typing import Optional

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
@click.option("--fps", type=float, default=500.0)
@click.option("--width", type=int, default=100)
@click.option("--height", type=int, default=100)
@click.option("--policy", "policy_str", type=str, default=None)
@click.option("--nth", "nth_frame", type=int, default=1)
@click.option("--debug", type=bool, is_flag=True)
def run(
    filepath: Path,
    iterations: int,
    fps: float,
    width: int,
    height: int,
    policy_str: Optional[str],
    nth_frame: int,
    debug: bool = False,
) -> None:
    set_logging_config(debug)

    with Graphics.context(filepath=filepath, width=width, height=height, fps=fps) as graphics:
        if policy_str is None:
            policy = Policy.from_str("R L L L L R R R L L L")
        else:
            policy = Policy.from_str(policy_str)

        with Simulation.context(
            graphics=graphics,
            iterations=iterations,
            width=width,
            height=height,
            nth_frame=nth_frame,
        ) as simulation:
            print(f"Running simulation for {iterations} iterations")
            simulation.run(policy)

        print(f"Saved to {filepath}")
