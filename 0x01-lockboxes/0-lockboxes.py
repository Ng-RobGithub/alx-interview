#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # If no boxes are provided, return False
    if not boxes:
        return False

    # Initialize a set to store keys and a set to store unlocked boxes
    keys = set(boxes[0])
    unlocked = set([0])

    # Perform a BFS traversal to unlock all possible boxes
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            keys.update(boxes[key])
            unlocked.add(key)

    # Return True if all boxes are unlocked, otherwise False
    return len(unlocked) == len(boxes)
