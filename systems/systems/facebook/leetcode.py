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
from systems.nodes import nextJs, Pytorch

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
        graph_attr={
            "newrank": "true",
            "fontname": "Times New Roman",
        },
    ):
        with Cluster(
            "external",
            graph_attr={
                "rank": "same",
                "bgcolor": "#ffffff",
                "pencolor": "#ffffff",
                "fontcolor": "#ffffff",
            },
        ):
            internet = Internet("Internet")
            static_contents_storage = SimpleStorageServiceS3Bucket(
                "Static contents"
            )
            cdn = CloudFront("CDN")
            internet >> cdn
            cdn >> static_contents_storage
        with Cluster("internal", graph_attr={"fontcolor": "#ffffff"}):
            bff = Spring("BFF")

            internet >> [nextJs("Frontend"), bff]

            timeline = Spring("Timeline")

            friendship = Spring("Friendship")
            friendship >> Redis("Cache")

            timeline >> friendship
            friendship >> Postgresql("DB")
            user = Spring("User")
            user_add_delete = Kafka("adding and deletion of users")
            [user, friendship] >> user_add_delete

            user >> Postgresql("DB")
            access_events = Kafka("User access events")
            user >> access_events
            post = Spring("Post")
            posts = Kafka("posts")
            stored_posts = Kafka("stored posts")
            post >> stored_posts
            timeline >> stored_posts
            bff >> [user, post, timeline, friendship, posts]
            timeline >> bff
            bff >> internet
            post >> [
                posts,
                Cassandra("DB(like, posts, comments)"),
                Elasticsearch("Search"),
                Redis("Cache"),
                Cassandra("Activity logs"),
                static_contents_storage,
                access_events,
            ]
            timeline >> post


if __name__ == "__main__":
    draw(sys.argv[1])
