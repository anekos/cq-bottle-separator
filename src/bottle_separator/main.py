import cadquery as cq
from click_cadquery.git import version_number as ver
from pydantic import BaseModel


class Param(BaseModel):
    diameter: float = 80.0
    thickness: float = 5.0
    height: float = 60.0

    @property
    def filename(self) -> str:
        return f"v{ver()}-bottle-separator-{self.diameter}mm.stl"


def build(param: Param) -> cq.Workplane:
    base = cq.Workplane("XY").circle(param.diameter / 2).extrude(param.thickness)

    separator = (
        cq.Workplane("XY")
        .workplane(offset=param.thickness)
        .rect(param.diameter, param.thickness)
        .extrude(param.height)
    )

    result = base.union(separator)

    return result
