"""Amazon System Design.

https://leetcode.com/explore/featured/card/system-design/690/system-design-case-studies/4384/
"""
import sys
import diagrams
from diagrams import Cluster, Edge
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


def draw(filepath: str):
    """Draw a diagram."""
    with diagrams.Diagram(
        "Amazon",
        show=False,
        filename=sys.argv[1],
        outformat="svg",
        direction="TB",
        graph_attr={"newrank": "true", "fontname": "Times New Roman"},
    ):
        with Cluster(
            "external",
            graph_attr={
                "rank": "same",
                "bgcolor": "#ffffff",
                "pencolor": "#ffffff",
                "fontcolor": "white",
            },
        ):
            internet = Internet("Internet")
            payment_services = Server("Payment Services")
            internet >> Edge(color="blue") >> payment_services
        with Cluster(" "):

            frontend = NextJs("frontend")
            bff = Spring("BFF")
            internet >> [bff, frontend]

            recommender = Fastapi("Recommendation")

            product = Spring("Product")
            inventry = Spring("Inventry")
            eta = Spring("Delivery ETA")
            eta >> [inventry, product]

            # 在庫をなくすときに、InventryからProductにリクエストを送る必要がある？
            inventry >> [product, Postgresql("DB")]
            # OAuth2の認証サーバを置く
            product >> [Redis("Cache"), Mongodb("DB"), Elasticsearch("Search")]
            user = Spring("User")
            user_db = Postgresql("DB")
            user >> user_db
            cart = Spring("Cart")
            cart >> [inventry, Cassandra("DB"), user]
            wishlist = Spring("Wishlist")
            wishlist >> [inventry, user, Cassandra("DB")]
            payment = Spring("Payment")
            bff >> [
                product,
                recommender,
                inventry,
                eta,
                wishlist,
                cart,
                payment,
            ]
            log_queue = Kafka("Log queue")
            [frontend, bff, payment, wishlist, cart] >> log_queue
            log_aggregator = Spark("Log aggregation")
            log_queue >> log_aggregator
            log_storage = SimpleStorageServiceS3Bucket("Log Storage")
            log_aggregator >> log_storage

            payment >> Edge(color="blue") >> internet
            payment >> [inventry, user, cart]
            order_history = Spring("Order history")
            payment >> order_history

            order_history >> Cassandra("DB")
            trainer = Pytorch("Recommendation Trainer")
            trainer >> log_storage


if __name__ == "__main__":
    draw(sys.argv[1])
