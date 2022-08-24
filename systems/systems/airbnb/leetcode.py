"""Airbnb System Design."""
import sys
from hornet.digraph import Digraph, SubGraph
from systems.nodes import Kafka


def draw(filepath: str):
    """Draw a diagram."""
    # Cleanup True as default
    with Digraph(f"{filepath}.svg", {}, cleanup=True):
        with SubGraph({"rank": "same"}):
            Kafka("queue")


if __name__ == "__main__":
    draw(sys.argv[1])
