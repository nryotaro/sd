"""Expose the root class to draw diggraphs."""
from graphviz import Digraph as _Digraph
import systems.hornet.state as _state
import systems.hornet.protocol as _protocol


class Digraph:
    """Represent a digraph."""

    def __enter__(self):
        """Declare a graph."""
        self._dot = _Digraph(filename="doge.gv", format="png")
        _state.put_graph(self)

    def __exit__(self, exc_type, exc_value, traceback):
        """Termination."""
        # https://graphviz.readthedocs.io/en/stable/api.html#graphviz.Graph.render
        self._dot.render()

    def put_node(self, node: _protocol.NodeProtocol):
        """Put a node."""
        self._dot.node(node.identity)


_states = dict()
