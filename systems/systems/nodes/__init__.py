"""Provide Custom classes with icons."""
import os.path
from diagrams.custom import Custom
from hornet.node import Node


def _resolve(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def NextJs(name: str) -> Custom:
    """Return a Custom object with Next.js logo."""
    return Custom(name, _resolve("nextjs.svg"))


def Pytorch(name: str) -> Custom:
    """Return a Custom object with Pytorch logo."""
    return Custom(name, _resolve("pytorch.svg"))


def Kafka(name: str) -> Node:
    """Return kafika."""
    return Node(name, {"image": _resolve("kafka.svg")})
