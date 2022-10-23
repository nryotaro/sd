"""Notication Service System Design."""
import sys
from hornet.digraph import Digraph, Cluster
from systems.nodes import (
    Internet,
    NextJs,
    Spring,
    PostgreSQL,
    Cassandra,
    Kafka,
    Redis,
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
            ui = NextJs("UI")
            auth = Spring("Authentication")
            internet >> [ui, auth]
            api_gateway = Spring("API Gateway")
            ui >> api_gateway
            user = Spring("User")
            postgres = PostgreSQL("User")
            [auth, api_gateway] >> user >> postgres
            config = Spring("Configuration")
            config >> PostgreSQL("Configuration")
            gateway = Spring("Gateway")
            gateway >> Redis("Recent requests")
            history = Spring("History")
            api_gateway >> [gateway, config, history]
            history >> Cassandra("History")
            requests_queue = Kafka("Requests")

            gateway >> requests_queue
            processed_requests = Kafka("Processed\nrequests")
            history >> processed_requests
            with Cluster({"label": "Handers"}):
                android = Spring("Android")
                mail = Spring("Mail")
                mail >> [
                    internet,
                    requests_queue,
                    processed_requests,
                ]
                android >> [
                    internet,
                    requests_queue,
                    processed_requests,
                ]
            config >> [android, mail]
