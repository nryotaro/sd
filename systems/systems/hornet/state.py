"""States for graphs."""
from systems.hornet.protocol import NodeProtocol, GraphProtocol

_state = []


def put_graph(graph: GraphProtocol):
    """Register a graph."""
    _state.append(graph)


def put_node(node: NodeProtocol):
    """Put a node on the current graph."""
    graph: GraphProtocol = _state[-1]
    graph.put_node(node)
