"""Google Maps.

This diagram is originated from System Design Inteview.

"""
import sys
from hornet.digraph import Digraph, Cluster
from systems.nodes import (
    Kafka,
    Cassandra,
    Mobile,
    Spring,
    HAProxy,
    NodeJs,
    FastAPI,
    Redis,
    S3,
)


if __name__ == "__main__":
    with Digraph(
        sys.argv[1],
        {
            "dpi": "350",
            "splines": "ortho",
            "newrank": "true",
            "fontname": "Times New Roman",
        },
    ):
        mobile = Mobile("Mobile")
        with Cluster():
            location_service = NodeJs("Location Service")
            (
                mobile
                >> HAProxy("Load Balancer")
                >> location_service
                >> Cassandra("User Location DB")
            )
            queue = Kafka("location")
            location_service >> queue
            traffic_db = Cassandra("Traffic DB")
            queue >> Spring("Traffic Update") >> traffic_db

            (
                queue
                >> FastAPI("Machine Learning\nfor Personalization")
                >> Cassandra("Personalization DB")
            )
            routing_tiles = S3("Routing Tiles")
            queue >> Spring("Routing Tile\nProcessing") >> routing_tiles
            queue >> Spring("Analytics") >> Cassandra("Analytics DB")

            navigation = NodeJs("Navigation")
            adaptive = Spring("Adaptive ETA and\nRouting")
            (navigation >> adaptive >> Redis("Active Users"))

            (
                mobile
                >> HAProxy("Load Balancer")
                >> navigation
                >> Spring("Geocoding")
                >> Redis("Geocoding DB")
            )
            route_planer = Spring("Route Planer")
            navigation >> route_planer
            ranker = Spring("Ranker")
            ranker >> Spring("Filter")
            shortest = Spring("Shortest Path")
            shortest >> routing_tiles
            eta = Spring("ETA")
            [adaptive, eta] >> traffic_db
            route_planer >> [ranker, shortest, eta]
