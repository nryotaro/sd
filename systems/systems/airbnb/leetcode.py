"""Airbnb System Design."""
import sys
from hornet.digraph import Digraph, SubGraph
from systems.nodes import Kafka, Internet, NextJs, Alb, ApiGateway


if __name__ == "__main__":
    """Draw an Airbnb system architecture."""
    with Digraph(
        sys.argv[1], {"dpi": "350", "splines": "true"}, cleanup=False
    ):
        internet = Internet("Internet")
        frontend = NextJs("Frontend")
        internet > frontend
        Alb("Load Balancer")
        ApiGateway("API Gateway")
        with SubGraph({"rank": "same"}):
            Kafka("queue")
