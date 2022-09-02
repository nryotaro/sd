"""Airbnb System Design."""
import sys
from hornet.digraph import Digraph, SubGraph
from systems.nodes import (
    Kafka,
    Elasticsearch,
    Internet,
    NextJs,
    Alb,
    Redis,
    HAProxy,
    Spring,
    PostgreSQL,
)


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
            api_gateway = Spring("API Gateway")
            frontend > api_gateway
        internet > HAProxy("Load Balancer") > frontend

        internet > api_gateway
        api_gateway > Spring("User") > PostgreSQL("DB")
        hotel = Spring("Hotel")
        api_gateway > hotel > PostgreSQL("DB")

        booking = Spring("Booking")
        api_gateway > booking
        api_gateway > Spring("Hotel") > [
            PostgreSQL("DB"),
            Redis("Cache"),
            Elasticsearch("Search"),
        ]

        booking > [PostgreSQL("DB")]

        [hotel, booking] > Kafka("user activities")
        # with SubGraph({"rank": "same"}):
        #     Kafka("queue")
