"""Provide Custom classes with icons."""
import os.path
from diagrams.custom import Custom


def _resolve(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def NextJs(name: str) -> Custom:
    """Return a Custom object with Next.js logo."""
    return Custom(name, _resolve("nextjs.svg"))
