import hou

from typing import Dict, List, Any


def serialize_as_dict(color: hou.Color) -> Dict[str, float]:
    return dict(zip(["r", "g", "b"], list(color.rgb())))


def deserialize_from_dict(color_data: Dict[str, float]) -> hou.Color:
    return hou.Color(tuple(color_data.values()))
