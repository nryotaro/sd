"""An overview of Google Maps.

https://leetcode.com/explore/featured/card/system-design/690/system-design-case-studies/4386/

"""
import diagrams
from diagrams.onprem import network as _network
from diagrams.elastic import elasticsearch as _es
from diagrams.onprem import analytics as _analytics
from diagrams.onprem import inmemory as _inmemory
from diagrams.programming import framework as _framework
from diagrams.onprem import queue as _queue
import diagrams.aws.network
import diagrams.onprem.database
import diagrams.generic.storage as _storage


with diagrams.Diagram(
    "GoogleMaps",
    show=False,
    outformat="pdf",
    direction="TB",
):
    internet = _network.Internet("Internet")
    data_provider = _storage.Storage(
        "Data Provider\n(e.g., map, traffic, weather)"
    )
    internet >> diagrams.aws.network.CF("CDN\nStatic contents")

    with diagrams.Cluster(
        "System boundary",
    ):
        mobile_bff = _network.Tomcat("Mobile BFF")
        browser_bff = _network.Tomcat("Browser BFF")
        frontend = _framework.React("Frontend")
        internet >> [mobile_bff, frontend, browser_bff]
        with diagrams.Cluster(
            "Map servie\nDraw maps",
        ):
            map_api = _network.Tomcat("Web API")
            map_update_requests_queue = _queue.Kafka("Update requests")
            map_api >> map_update_requests_queue
            map_update = _analytics.Spark("Update")
            (
                map_update
                >> diagrams.Edge(color="brown")
                >> internet
                >> diagrams.Edge(color="brown", label="Get the lastest data")
                >> data_provider
            )
            map_cache = _inmemory.Redis("Cache")
            map_api >> map_cache
            map_update >> map_cache
            map_update >> map_update_requests_queue
            location_search_engine = _es.Elasticsearch(
                "Search engine\nQuery addresses by names"
            )
            map_update >> location_search_engine
            map_api >> location_search_engine
            map_update >> location_search_engine
            [mobile_bff, browser_bff] >> map_api

            with diagrams.Cluster(
                "Database (data for drawing maps)",
            ):
                diagrams.onprem.database.Cassandra("World"),
                diagrams.onprem.database.Cassandra("Country")
                map_town_db = diagrams.onprem.database.Cassandra("Town")

                map_api >> map_town_db
                map_update >> map_town_db

        map_update_queue = _queue.Kafka("Updated area")
        map_update >> map_update_queue

        with diagrams.Cluster(
            "Graph service\nFind the distance and ETA of two points"
        ):
            graph_api = _network.Tomcat("Web API")
            graph_update = _analytics.Spark("Update")
            map_update_queue << graph_update
            with diagrams.Cluster("Database"):

                diagrams.onprem.database.Cassandra("World")
                graph_country_db = diagrams.onprem.database.Cassandra(
                    "Country"
                )
                diagrams.onprem.database.Cassandra("Town")

                graph_api >> graph_country_db
                graph_update >> graph_country_db

            [mobile_bff, browser_bff] >> graph_api
            eta_queue = _queue.Kafka("ETA\nupdate requests")
            graph_update >> eta_queue
            path_eta_calc = _analytics.Spark("Path and ETA\nCalculator")
            eta_queue << path_eta_calc
            path_eta_calc >> graph_country_db
            graph_cache = _inmemory.Redis("Cache")
            graph_api >> graph_cache
            path_eta_calc >> graph_cache
