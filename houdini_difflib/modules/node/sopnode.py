import hou

from typing import Dict, List, Any

from houdini_difflib.modules.node import node


def serialize_as_dict(sop_node_instance: hou.SopNode) -> Dict[str, Any]:
    return {
        **node.serialize_as_dict(sop_node_instance),
        "isDisplayFlagSet": sop_node_instance.isDisplayFlagSet(),
        "isRenderFlagSet": sop_node_instance.isRenderFlagSet(),
        "isTemplateFlagSet": sop_node_instance.isTemplateFlagSet(),
    }


def deserialize_from_dict(
    node_data: Dict[str, Any], parent: hou.Node
) -> hou.Node:
    node_instance = node.deserialize_from_dict(node_data, parent)

    if isinstance(node_instance, hou.SopNode):
        node_instance.setDisplayFlag(node_data["isDisplayFlagSet"])
        node_instance.setRenderFlag(node_data["isRenderFlagSet"])
        node_instance.setTemplateFlag(node_data["isTemplateFlagSet"])

    return node_instance
