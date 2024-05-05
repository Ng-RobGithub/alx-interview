#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    """ Set of keys initially available"""
    keys = set(boxes[0])

    """ Set of unlocked boxes"""
    unlocked = set([0])

    """ Breadth-first search to traverse through boxes and keys"""
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            keys.update(boxes[key])
            unlocked.add(key)

    return len(unlocked) == len(boxes)
