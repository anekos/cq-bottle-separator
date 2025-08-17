from pathlib import Path

import cadquery.vis as vis
import click
from click_cadquery import define_options

from .main import Param, build

TypePath = click.types.Path(path_type=Path)


@click.group()
@click.pass_context
def main(ctx: click.Context) -> None:
    # ctx.obj = App()
    pass


@main.command(name="build")
@define_options(Param)
def command_build(output: Path | None, param: Param, show: bool) -> None:
    print("Build with:", param)

    result = build(param)

    dist = Path("dist")
    dist.mkdir(exist_ok=True)
    result.export(str(output if output else dist / param.filename))
    if show:
        vis.show(result, axes=True, axes_length=10)
