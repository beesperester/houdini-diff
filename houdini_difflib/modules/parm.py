import hou

from typing import Dict, List, Any, Union


def serialize_as_dict(parm: hou.Parm) -> Dict[str, Any]:
    return {
        "name": parm.name(),
        "description": parm.description(),
        "isLocked": parm.isLocked(),
        "isSpare": parm.isSpare(),
        "rawValue": parm.rawValue(),
    }
