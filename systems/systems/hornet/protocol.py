"""Define protocols."""
import typing


class NodeProtocol(typing.Protocol):
    """"""

    @property
    def identity(self) -> str:
        """id of a node."""


class GraphProtocol(typing.Protocol):
    def put_node(self, node: NodeProtocol):
        """Put a node."""
