import hou

from typing import Dict, List, Any, Union

from houdini_difflib.modules import (
    color,
    nodetype,
    vector2,
    parm,
    nodeconnection,
)

from houdini_difflib.modules import node, nodes

from houdini_difflib.modules.node import sopnode, objnode


def serialize_as_dict(node_instance: hou.Node) -> Dict[str, Any]:
    return {
        "class_name": node_instance.__class__.__name__,
        "name": node_instance.name(),
        "type": nodetype.serialize_as_dict(node_instance.type()),
        "color": color.serialize_as_dict(node_instance.color()),
        "position": vector2.serialize_as_dict(node_instance.position()),
        "parms": {
            x.name(): parm.serialize_as_dict(x)
            for x in list(node_instance.parms())
            if not x.isAtDefault(
                compare_temporary_defaults=True, compare_expressions=False
            )
        },
        "inputConnections": [
            nodeconnection.serialize_as_dict(x)
            for x in list(node_instance.inputConnections())
        ],
        "isNetwork": node_instance.isNetwork(),
        "children": nodes.serialize_as_dict(list(node_instance.children()))
        if node_instance.isNetwork()
        else {},
    }


def deserialize_from_dict(
    node_data: Dict[str, Any], parent: hou.Node
) -> hou.Node:
    node_instance: hou.Node = parent.node(node_data["name"])

    if not node_instance:
        node_instance = parent.createNode(
            node_type_name=node_data["type"]["name"],
            node_name=node_data["name"],
        )

    node_instance.setPosition(
        vector2.deserialize_from_dict(node_data["position"])
    )

    # apply parameter changes
    exceptions: List[str] = []

    for parm_name, parm_data in node_data["parms"].items():
        parm: hou.Parm = node_instance.parm(parm_name)

        try:
            if parm:
                node_instance.parm(parm_name).set(parm_data["rawValue"])
        except TypeError:
            exceptions.append(parm_data)

    if exceptions:
        print(
            "Unable to set the following parameters on '{}': {}".format(
                node_instance.name(), ", ".join(exceptions)
            )
        )

    # deserialize children
    children = nodes.deserialize_from_dict(
        node_data["children"].values(), node_instance
    )

    return node_instance
