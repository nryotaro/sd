"""Netflix System Design.

https://leetcode.com/explore/learn/card/system-design/690/system-design-case-studies/4388/
"""
import sys
from hornet.digraph import Digraph, SubGraph, Cluster

if __name__ == "__main__":
    with Digraph(
        sys.argv[1],
        {
            "dpi": "350",
            "splines": "true",
            "newrank": "true",
            "fontname": "Times New Roman",
        },
    ):
        ...
