import hou

from typing import Dict, List, Any

from houdini_difflib.modules.node import objnode, sopnode


def serialize_as_dict(node_instance: hou.Node) -> Dict[str, Any]:
    if isinstance(node_instance, hou.ObjNode):
        return objnode.serialize_as_dict(node_instance)
    elif isinstance(node_instance, hou.SopNode):
        return sopnode.serialize_as_dict(node_instance)
    else:
        return serialize_as_dict(node_instance)


def deserialize_from_dict(
    node_data: Dict[str, Any], parent: hou.Node
) -> hou.Node:
    if node_data["class_name"] == "ObjNode":
        return objnode.deserialize_from_dict(node_data, parent)
    elif node_data["class_name"] == "SopNode":
        return sopnode.deserialize_from_dict(node_data, parent)
    else:
        return deserialize_from_dict(node_data, parent)
