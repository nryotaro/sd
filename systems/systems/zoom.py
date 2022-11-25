"""Zoom.."""
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

        with Cluster():
            stun = NodeJs("STUN")
            turn = NodeJs("TURN")
            online = NodeJs("Online(WebSocket)")
            user >> [stun, turn, online]
            online_manager = NodeJs("Online Manager")
            online_manager >> Redis("Cache")
            offline_caller = Spring("Offline caller")
            online >> [online_manager, offline_caller]
            turn >> Spring("Recoder")
            turn >> Spring("Transcoder")
