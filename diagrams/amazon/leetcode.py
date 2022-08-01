"""Amazon System Design.

https://leetcode.com/explore/featured/card/system-design/690/system-design-case-studies/4384/
"""
import sys
import diagrams
from diagrams import Cluster
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mongodb, Postgresql
from diagrams.onprem.inmemory import Redis
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.programming.framework import React, Spring, Fastapi


with diagrams.Diagram(
    "Amazon",
    show=False,
    filename=sys.argv[1],
    outformat="svg",
    direction="TB",
):
    internet = Internet("Internet")

    payment_services = Server("Payment Services")

    internet >> payment_services

    with Cluster(""):
        frontend = React("Frontend")
        bff = Spring("BFF")
        internet >> [bff, frontend]

        recommender = Fastapi("Recommendation")
        product = Spring("Product")
        inventry = Spring("Inventry")

        eta = Spring("Delivery ETA")
        eta >> [inventry, product]
        bff >> [product, recommender, inventry, eta]

        inventry >> [product, Postgresql("DB")]

        product >> [Redis("Cache"), Mongodb("DB"), Elasticsearch("Search")]
