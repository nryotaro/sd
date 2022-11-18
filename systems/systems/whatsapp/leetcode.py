"""Airbnb System Design."""
import sys
from hornet.digraph import Digraph, Cluster
from systems.nodes import (
    Kafka,
    NodeJs,
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
        user = User("User")
        media = S3("Media")
        cdn = CloudFront("CDN")
        user >> cdn >> media
        with Cluster():
            online_monitor = NodeJs("Online Monitor")
            online_manager = Spring("Online Manager")
            message = Spring("Message")
            online_monitor >> [media, message]
            user >> online_monitor >> online_manager >> Redis("Online users")
            message >> Cassandra("Message")
            (
                online_monitor
                >> Spring("seen histroy")
                >> Cassandra("Last histroy")
            )
