import click
import importlib
from time import time


@click.command()
@click.argument("year")
@click.argument("problem")
@click.argument("part")
def cli(year, problem, part):
    module = importlib.import_module(f"src.{year}.{problem}.{part}")
    t0 = time()
    click.echo(module.solution())
    click.echo(time() - t0)
