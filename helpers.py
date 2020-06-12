"""Helper classes and functions for the route planner.

Classes:
    Map()
"""

import pickle

import networkx as nx


class Map:
    """Create a map as a graph with intersections as nodes and roads as edges.

    Attributes:
        _graph: The graph representation
        intersections: A dict of lists representing the x, y coordinates of
            the nodes in the graph
        roads: A list of lists representing all the nodes that a node at each
            index is directly connected to
    """

    def __init__(self, graph):
        """Set-up for the map."""
        self._graph = graph
        self.intersections = nx.get_node_attributes(graph, "pos")
        self.roads = [list(graph[node]) for node in graph.nodes()]

    def save(self, filename):
        """Save the map into a pickle.

        Args:
            filename: A str representing the name of the file to save the
                map to
        """
        with open(filename, "wb") as f:
            pickle.dump(self._graph, f)


def load_map(name):
    """Load a map from a pickle.

    Args:
        name: A str representing the name of the file to load the map from
    """
    with open(name, "rb") as f:
        graph = pickle.load(f)
    return Map(graph)
