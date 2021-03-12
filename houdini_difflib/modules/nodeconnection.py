import hou

from typing import Dict, List, Any, Union


def serialize_as_dict(
    connection: hou.NodeConnection,
) -> Dict[str, Union[str, int]]:
    return {
        "outputNode": connection.outputNode().name(),
        "inputNode": connection.inputNode().name(),
        "outputIndex": connection.outputIndex(),
        "inputIndex": connection.inputIndex(),
    }
