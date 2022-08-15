"""Expose a node."""
from systems.hornet import state as _state


class Node:
    """Implement `NodeProtocol`."""

    def __init__(self, identity: str):
        """Put a node in a graph."""
        self.identity = identity
        _state.put_node(self)
