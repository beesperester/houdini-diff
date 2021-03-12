from typing import Any, Dict


import hou

from typing import Dict, List, Any

from houdini_difflib.modules import node


def serialize_as_dict(node_instances: List[hou.Node]) -> Dict[str, Any]:
    return {
        node_instance.name(): node.serialize_as_dict(node_instance)
        for node_instance in node_instances
    }


def deserialize_from_dict(
    nodes_data: List[Dict[str, Any]], parent: hou.Node
) -> List[hou.Node]:
    nodes = []

    for node_data in nodes_data:
        node_instance = node.deserialize_from_dict(node_data, parent)

        nodes.append(node_instance)

    # create connections
    for node_data in nodes_data:
        node_instance: hou.Node = parent.node(node_data["name"])

        if node_instance:
            for connection_data in node_data["inputConnections"]:
                input_node = parent.node(connection_data["inputNode"])

                if input_node:
                    node_instance.setInput(
                        input_index=connection_data["inputIndex"],
                        item_to_become_input=input_node,
                        output_index=connection_data["outputIndex"],
                    )

    return nodes
