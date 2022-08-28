"""Provide Custom classes with icons."""
import os.path
import uuid
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


def _create_node(name: str, image_file_name: str) -> Node:
    height = 1.6 + 0.4 * name.count("\n")

    return Node(
        uuid.uuid4().hex[:4],
        {
            "imagescale": "true",
            "imagepos": "tc",
            "fixedsize": "true",
            "label": name,
            "labelloc": "b",
            "shape": "none",
            "width": "1.4",
            "height": f"{height}",
            "image": _resolve(image_file_name),
        },
    )
