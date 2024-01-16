import logging

import click

from langton.lib.ant import Ant
from langton.lib.video import generate_video

logger = logging.getLogger(__name__)


@click.group()
def main() -> None:
    """Main CLI entrypoint."""


@main.command()
def run() -> None:
    ant = Ant()
    print("Running", ant)
    generate_video()
