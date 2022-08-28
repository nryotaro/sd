"""Airbnb System Design."""
import sys
from hornet.digraph import Digraph, SubGraph
from systems.nodes import Kafka, Internet, NextJs, Alb, ApiGateway


if __name__ == "__main__":
    """Draw an Airbnb system architecture."""
    with Digraph(
        sys.argv[1],
        {
            "dpi": "350",
            "splines": "true",
            "newrank": "true",
            "fontname": "Times New Roman",
        },
        cleanup=False,
    ):
        internet = Internet("Internet")
        with SubGraph({"rank": "same"}):
            frontend = NextJs("Frontend")
            api_gateway = ApiGateway("API Gateway")
            frontend > api_gateway
        internet > Alb("Load Balancer") > frontend
        internet > api_gateway

        with SubGraph({"rank": "same"}):
            Kafka("queue")
