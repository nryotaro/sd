"""Provide Custom classes with icons."""
import os.path
from diagrams.custom import Custom
from hornet.node import Node


def _resolve(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def nextJs(name: str) -> Custom:
    """Return a Custom object with Next.js logo."""
    return Custom(name, _resolve("nextjs.svg"))


def Pytorch(name: str) -> Custom:
    """Return a Custom object with Pytorch logo."""
    return Custom(name, _resolve("pytorch.svg"))


def Kafka(name: str) -> Node:
    """Kafka."""
    return _create_node(name, "kafka.svg")


def Internet(name: str) -> Node:
    """Internet."""
    return _create_node(name, "internet.svg")


def NextJs(name: str) -> Node:
    """NextJs."""
    return _create_node(name, "nextjs.svg")


def Alb(name: str) -> Node:
    """Application Load Balancer."""
    return _create_node(name, "alb.svg")


def ApiGateway(name: str) -> Node:
    """AWS gateway."""
    return _create_node(name, "api_gateway.svg")


def Spring(name: str) -> Node:
    """Spring."""
    return _create_node(name, "spring.svg")


def PostgreSQL(name: str) -> Node:
    """PostgreSQL."""
    return _create_node(name, "postgresql.svg")


def User(name: str) -> Node:
    """User."""
    return _create_node(name, "user.svg")


def Python(name: str) -> Node:
    """Python."""
    return _create_node(name, "python.svg")


def Redis(name: str) -> Node:
    """Redis."""
    return _create_node(name, "redis.svg")


def CloudFront(name: str) -> Node:
    """CloudFront."""
    return _create_node(name, "cloudfront.svg")


def S3(name: str) -> Node:
    """S3."""
    return _create_node(name, "s3.svg")


def HAProxy(name: str) -> Node:
    """HAProxy."""
    return _create_node(name, "haproxy.svg")


def Cassandra(name: str) -> Node:
    """Redis."""
    return _create_node(name, "cassandra.svg")


def Elasticsearch(name: str) -> Node:
    """Elasticsearch."""
    return _create_node(name, "elasticsearch.svg")


def _create_node(
    name: str, image_file_name: str, base_height: int = 2.0, width: int = 1.6
) -> Node:
    height = base_height + 0.4 * name.count("\n")

    return Node(
        name,
        {
            "imagescale": "true",
            "imagepos": "tc",
            "fixedsize": "true",
            "labelloc": "b",
            "shape": "none",
            "width": f"{width}",
            "height": f"{height}",
            "image": _resolve(image_file_name),
        },
    )
