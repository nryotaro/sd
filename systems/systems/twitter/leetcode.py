"""Airbnb System Design."""
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
        user = User("User")
        media = S3("Media")
        user >> CloudFront("CDN") >> media
        with Cluster():
            ui = NextJs("UI")

            user >> ui >> Spring("User") >> PostgreSQL("DB")
            timeline = Spring("Timeline")
            timeline >> Redis("Cache")
            persistence = Spring("Tweet Persistence")
            persistence >> timeline
            persistence >> media
            tweet = Spring("Tweet")
            timeline >> tweet
            tweet_msg = Kafka("Tweet")
            ingestion = Spring("Tweet Ingestion")
            ingestion >> tweet_msg << persistence
            ui >> [timeline, ingestion]
            [persistence, tweet] >> Cassandra("DB")
            [persistence, tweet] >> Redis("Cache")
            [persistence, tweet] >> Elasticsearch("Search")
