"""An overview of Google Maps.

https://leetcode.com/explore/featured/card/system-design/690/system-design-case-studies/4386/

"""
import diagrams
from diagrams.onprem import network as _network
from diagrams.onprem import compute as _compute
from diagrams.elastic import elasticsearch as _es
from diagrams.onprem import analytics as _analytics
from diagrams.onprem import inmemory as _inmemory
from diagrams.onprem import queue as _queue
import diagrams.aws.network
import diagrams.onprem.database
import diagrams.generic.storage as _storage


with diagrams.Diagram(
    "GoolgeMaps", show=False, outformat="pdf", direction="TB"
):
    with diagrams.Cluster(
        "",
        direction="LR",
        graph_attr={
            "bgcolor": "transparent",
            "shape": "none",
            "style": "invis",
        },
    ):
        internet = _network.Internet("Internet")
        data_provider = _storage.Storage(
            "Data Provider\n(e.g., map, traffic, weather)"
        )
        internet >> diagrams.aws.network.CF("CDN")

    with diagrams.Cluster("System boundary"):
        mobile_bff = _compute.Server("Mobile BFF")
        browser_bff = _compute.Server("Browser BFF")
        frontend = _compute.Server("Frontend")
        internet >> [mobile_bff, frontend, browser_bff]

        with diagrams.Cluster("Map servie(e.g., building, road, station)"):
            map_api = _network.Tomcat("Web API")
            map_update = _analytics.Spark("Update")
            (
                map_update
                >> diagrams.Edge(color="brown")
                >> internet
                >> diagrams.Edge(color="brown")
                >> data_provider
            )
            location_search_engine = _es.Elasticsearch(
                "Location Search engine"
            )
            map_api >> location_search_engine
            map_update >> location_search_engine
            [mobile_bff, browser_bff] >> map_api

            with diagrams.Cluster("Database"):
                map_databases = [
                    diagrams.onprem.database.Cassandra("World"),
                    diagrams.onprem.database.Cassandra("Country"),
                    diagrams.onprem.database.Cassandra("Town"),
                ]
                map_api >> map_databases
                map_update >> map_databases
                map_cache = _inmemory.Redis("Cache")
                map_api >> map_cache
                map_update >> map_cache

        map_update_queue = _queue.Kafka("Updated area")
        map_update >> map_update_queue

        with diagrams.Cluster("Graph"):
            graph_api = _network.Tomcat("Web API")
            graph_update = _analytics.Spark("Update")
            map_update_queue << graph_update
            with diagrams.Cluster("Database"):
                graph_databases = [
                    diagrams.onprem.database.Cassandra("World"),
                    diagrams.onprem.database.Cassandra("Country"),
                    diagrams.onprem.database.Cassandra("Town"),
                ]
                graph_api >> graph_databases
                graph_update >> graph_databases

            [mobile_bff, browser_bff] >> graph_api
            eta_queue = _queue.Kafka("ETA\nupdate requests")
            graph_update >> eta_queue
            path_eta_calc = _analytics.Spark("Path and ETA\nCalculator")
            eta_queue << path_eta_calc
            path_eta_calc >> graph_databases
            graph_cache = _inmemory.Redis("Cache")
            graph_api >> graph_cache
            path_eta_calc >> graph_cache
