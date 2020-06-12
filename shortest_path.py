"""Find the shortest path between two nodes in a graph using the A* algorithm.

Usage: shortest_path.py

Classes:
    MinHeap()
"""

from test import test


class MinHeap:
    """Creates a min-heap where the minimum value is at the root of the tree.

    Attributes:
        heap: A list representing the items in the heap
    """

    def __init__(self):
        """Set-up for the min-heap."""
        self.heap = []

    def push(self, item):
        """Push an item onto the heap.

        Args:
            item: The item to push onto the heap
        """
        idx = len(self.heap)
        parent_idx = (idx - 1) // 2
        self.heap.append(item)

        while idx > 0 and self.heap[parent_idx] > self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[parent_idx],
            )
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def pop(self):
        """Pop the smallest item off the top of the heap.

        Returns:
            min_node: The smallest item (located at the root of the node)
        """
        if len(self.heap) == 0:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_node = self.heap.pop()
        idx = 0
        child_idx = 2 * idx + 1

        while (
            child_idx < len(self.heap)
            and self.heap[idx] > self.heap[child_idx]
        ):
            if (
                len(self.heap) > child_idx + 1
                and self.heap[child_idx] > self.heap[child_idx + 1]
            ):
                child_idx += 1

            self.heap[child_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[child_idx],
            )
            idx = child_idx
            child_idx = 2 * idx + 1

        return min_node


def main():
    """Main function call to test the shortest_path function."""
    test(shortest_path)


def shortest_path(graph, start, end):
    """Find the shortest path between nodes in a graph using the A* algorithm.

    Args:
        graph: A Map object representing the graph to find the shortest path
            within
        start: An int representing the node in the graph the path will start at
        end: An int representing the node in the graph the path will end at

    Returns:
        path: A list of ints representing the shortest path of nodes to
            traverse from the start node to the end node
    """
    visited = set()
    min_heap = MinHeap()

    distance = distance_between_nodes(graph, start, start)
    heuristic = distance_between_nodes(graph, start, end)
    estimated_distance = distance + heuristic
    min_heap.push((estimated_distance, distance, [start]))

    while len(min_heap.heap) > 0:
        _, distance, path = min_heap.pop()
        current_node = path[-1]
        visited.add(current_node)

        if current_node == end:
            return path

        for node in graph.roads[current_node]:
            if node not in visited:
                updated_distance = distance + distance_between_nodes(
                    graph, current_node, node
                )
                heuristic = distance_between_nodes(graph, node, end)
                estimated_distance = updated_distance + heuristic
                min_heap.push(
                    (estimated_distance, updated_distance, path + [node])
                )

    return None


def distance_between_nodes(graph, node_1, node_2):
    """Calculate the distance between two nodes in a given graph.

    Args:
        graph: A Map object representing the graph containing the nodes to find
            the distance between
        node_1: An int representing the first node in the pair of nodes to find
            the distance between
        node_2: An int representing the second node in the pair of nodes to
            find the distance between

    Returns:
        distance: A float representing the distance between node_1 and node_2
            in the given graph
    """
    [x_1, y_1] = graph.intersections[node_1]
    [x_2, y_2] = graph.intersections[node_2]
    distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

    return distance


if __name__ == "__main__":
    main()
