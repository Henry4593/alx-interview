#!/usr/bin/python3
'''A module containing functions for managing secure lockboxes
'''


def canUnlockAll(boxes):
    """
    Determines if every box in a collection, each containing keys (indices) to
    other boxes, can be opened starting from the first box.
    """

    n = len(boxes)
    visited_boxes = {0}
    unvisited_boxes = set(boxes[0])

    while unvisited_boxes:
        boxIdx = unvisited_boxes.pop()
        if 0 <= boxIdx < n and boxIdx not in visited_boxes:
            unvisited_boxes.update(boxes[boxIdx])
            visited_boxes.add(boxIdx)

    return len(visited_boxes) == n
