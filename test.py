"""Test function to test the behavior of the shortest_path function.

Attributes:
    MAP_40_ANSWERS: A list of tuples representing the inputs and expected
        outputs of various test cases with the map_40 map stored in
        map-40.pickle
"""

from helpers import load_map

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5, [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),
]


def test(shortest_path_function):
    """Test function for the shortest_path function.

    Args:
        shortest_path_function: A func representing the A* algorithm
            implementation to find the shortest path between two nodes in a
            graph
    """
    map_40 = load_map("map-40.pickle")
    correct = 0
    for start, end, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, end)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start)
            print("End:      ", end)
            print("Your path:", path)
            print("Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
