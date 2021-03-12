import hou

from typing import Dict, List, Any


def serialize_as_dict(vector2: hou.Vector2) -> Dict[str, float]:
    return {"x": vector2.x(), "y": vector2.y()}


def deserialize_from_dict(vector2_data: Dict[str, float]) -> hou.Vector2:
    return hou.Vector2(tuple(vector2_data.values()))
