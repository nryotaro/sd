"""Draw my solution of Facebook System Design.

https://leetcode.com/explore/featured/card/system-design/690/system-design-case-studies/4385/
"""
import sys
import diagrams
from diagrams import Cluster, Edge
from diagrams.aws.network import CloudFront
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mongodb, Postgresql, Cassandra
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Spark
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.programming.framework import Spring, Fastapi
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from systems.nodes import NextJs, Pytorch

# from systems.hornet.digraph import Digraph
# from systems.hornet.node import Node


# def draw(filepath: str):
#     """Draw a diagram, and saves it to `filepath`."""
#     with Digraph():
#         Node("a")


def draw(filepath: str):
    """Draw system architecture."""
    with diagrams.Diagram(
        "Amazon",
        show=False,
        filename=filepath,
        outformat="svg",
        direction="TB",
        graph_attr={"newrank": "true"},
    ):
        with Cluster(
            "",
            graph_attr={
                "rank": "same",
                "bgcolor": "#ffffff",
                "pencolor": "#ffffff",
            },
        ):
            internet = Internet("Internet")
            cdn = CloudFront("CDN")
            internet >> cdn
        with Cluster():
            bff = Spring("BFF")
            internet >> [NextJs("Frontend"), bff]

            timeline = Spring("Timeline")
            user = Spring("User")
            friendship = Spring("Friendship")
            timeline >> friendship
            friendship >> Postgresql("DB")
            user >> Postgresql("DB")
            bff >> [timeline, user]
            post = Spring("Post")
            post >> [
                Cassandra("DB(like, posts, comments)"),
                Elasticsearch("Search"),
                Redis("Cache"),
                Cassandra("Activity logs"),
            ]

            cache_maintainer = Spring("Cache Maintainer")
            cache_maintainer >> [user, post]
            timeline >> post
            post >> cdn


if __name__ == "__main__":
    draw(sys.argv[1])
