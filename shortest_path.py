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


class LinkedList:
    """A linked list where each node points to the previous node.

    Attributes:
        tail: A Node object that represents the last node in the linked list
    """

    def __init__(self, tail):
        """Set-up for the linked list."""
        self.tail = tail

    def to_list(self):
        """Transforms the linked list node values to regular python list."""
        linked_list = []
        node = self.tail

        while node is not None:
            linked_list = [node.value] + linked_list
            node = node.prev

        return linked_list


class Node:
    """A node to store in a linked list.

    Attributes:
        value: The value to store in the node
        distance: An int representing the shortest known distance from the
            start node, defaults to infinity
        prev: A Node object representing the previous node in the linked list
    """

    def __init__(self, value, distance, prev=None):
        """Set-up for the linked list node."""
        self.value = value
        self.distance = distance
        self.prev = prev


def main():
    """Main function call to test the shortest_path function."""
    test(shortest_path)


def shortest_path(graph, start_id, end_id):
    """Find the shortest path between nodes in a graph using the A* algorithm.

    Args:
        graph: A Map object representing the graph to find the shortest path
            within
        start_id: An int representing the id of the node in the graph that the
            path will start at
        end_id: An int representing the id of the node in the graph the path
            will end at

    Returns:
        path: A list of ints representing the shortest path of nodes to
            traverse from the start node to the end node
    """
    visited = set()
    min_heap = MinHeap()

    distance = distance_between_nodes(graph, start_id, start_id)
    heuristic = distance_between_nodes(graph, start_id, end_id)
    estimated_distance = distance + heuristic
    min_heap.push((estimated_distance, Node(start_id, distance)))

    while len(min_heap.heap) > 0:
        node = min_heap.pop()[1]
        visited.add(node.value)

        if node.value == end_id:
            path = LinkedList(node).to_list()
            return path

        for node_id in graph.roads[node.value]:
            if node_id not in visited:
                distance = node.distance + distance_between_nodes(
                    graph, node.value, node_id
                )
                heuristic = distance_between_nodes(graph, node_id, end_id)
                estimated_distance = distance + heuristic
                min_heap.push(
                    (estimated_distance, Node(node_id, distance, node))
                )

    return None


def distance_between_nodes(graph, node_1_id, node_2_id):
    """Calculate the distance between two nodes in a given graph.

    Args:
        graph: A Map object representing the graph containing the nodes to find
            the distance between
        node_1_id: An int representing the id of the first node in the pair of
            nodes to find the distance between
        node_2_id: An int representing the id of the second node in the pair of
            nodes to find the distance between

    Returns:
        distance: A float representing the distance between node_1 and node_2
            in the given graph
    """
    [x_1, y_1] = graph.intersections[node_1_id]
    [x_2, y_2] = graph.intersections[node_2_id]
    distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

    return distance


if __name__ == "__main__":
    main()
