#!/usr/bin/python3
<<<<<<< HEAD
"""
A Python module to determine if all boxes can be opened from a list of lists.
"""
=======
>>>>>>> 73ea719f2861402683ddd8c17a09c4e2909e9334

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): List of lists containing keys in each box.

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

<<<<<<< HEAD

if __name__ == '__main__':
    boxes = [
        [1, 3],
        [2],
        [3, 0],
        [1, 2, 3],
    ]
    print(can_unlock_all(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(can_unlock_all(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(can_unlock_all(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(can_unlock_all(boxes))
=======
    return len(unlocked) == len(boxes)
>>>>>>> 73ea719f2861402683ddd8c17a09c4e2909e9334
