import hou

from typing import Dict, List, Any


def serialize_as_dict(type: hou.NodeType) -> Dict[str, str]:
    return {"name": type.name(), "sourcePath": type.sourcePath()}
