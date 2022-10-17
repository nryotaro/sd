"""Netflix System Design.

https://leetcode.com/explore/learn/card/system-design/690/system-design-case-studies/4388/
"""
import sys
from hornet.digraph import Digraph, Cluster, SubGraph
from systems.nodes import (
    Internet,
    CloudFront,
    NextJs,
    S3,
    Spring,
    PostgreSQL,
    Redis,
    Kafka,
    Elasticsearch,
    Cassandra,
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
        internet = Internet("Internet")

        with Cluster():
            cdn = CloudFront("CDN")
            internet >> cdn
            movies = S3("Movies")
            cdn >> movies

        with Cluster():
            with SubGraph({"rank": "same"}):
                ui = NextJs("Web UI")
                upload_api = Spring("Movie Upload API")
                user = Spring("User")
                player = Spring("Movie Player")
                upload_api >> player

            internet >> [ui, upload_api, user, player]
            user >> [PostgreSQL("DB"), Redis("Cache")]
            raw_videos = Kafka("Raw movies")
            encoder = Spring("Encoder")
            encoded = Kafka("Encoded moviews")
            upload_api >> raw_videos
            encoder >> [encoded, raw_videos]
            uploader = Spring("Uploader")
            progress = Kafka("Progress")
            upload_api >> progress
            uploader >> [encoded, movies, progress]
            search = Elasticsearch("Movie search")
            meta = Cassandra("Movie meta data")
            player >> [search, meta]
