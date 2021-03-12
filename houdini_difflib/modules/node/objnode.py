import hou

from typing import Dict, List, Any

from houdini_difflib.modules.node import node


def serialize_as_dict(obj_node: hou.ObjNode) -> Dict[str, Any]:
    return {
        **node.serialize_as_dict(obj_node),
        "isDisplayFlagSet": obj_node.isDisplayFlagSet(),
    }


def deserialize_from_dict(
    node_data: Dict[str, Any], parent: hou.Node
) -> hou.Node:
    node_instance = node.deserialize_from_dict(node_data, parent)

    if isinstance(node_instance, hou.ObjNode):
        node_instance.setDisplayFlag(node_data["isDisplayFlagSet"])

    return node_instance
