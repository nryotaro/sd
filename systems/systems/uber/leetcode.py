"""Uber System Design."""
import sys
from hornet.digraph import Digraph, Cluster
from systems.nodes import (
    Kafka,
    S3,
    Elasticsearch,
    Cassandra,
    CloudFront,
    NextJs,
    Redis,
    Spring,
    PostgreSQL,
    User,
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
        customer = User("Customer")
        driver = User("Driver")

        with Cluster():
            customer_api = Spring("Customer")
            customer >> customer_api >> PostgreSQL("Customer")
            driver_api = Spring("Driver")
            driver_api >> PostgreSQL("Driver")
            cab_api = Spring("Cab")
            cab_api >> PostgreSQL("Cab")
            driver >> [cab_api, driver_api]

            finder = Spring("Cab finder")
            cab_location = Spring("Cab Location")
            driver >> cab_location
            cab_location >> [Redis("Current Location"), Cassandra("Trip")]
            map_api = Spring("Map")
            map_api >> PostgreSQL("Map")
            customer >> finder >> [cab_location, map_api]

            book_api = Spring("Book")
            book_api >> PostgreSQL("Book")
            customer >> book_api >> [customer_api, driver_api]
