#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each sublist
        represents a box and contains integers representing the
        keys inside that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is initially unlocked
    keys = set(boxes[0])  # Start with the keys in the first box
    opened = [0]

    while opened:
        box_index = opened.pop()
        for key in boxes[box_index]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.update(boxes[key])
                opened.append(key)

    return all(unlocked)
