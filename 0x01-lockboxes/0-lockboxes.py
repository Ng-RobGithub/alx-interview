#!/usr/bin/python3
"""
A Python module to determine if all boxes can be opened from a list of lists.
"""


def can_unlock_all(boxes=[]):
    """
    Determine if all boxes in the list can be opened.

    Args:
        boxes (list): List of lists containing keys in each box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set([0])
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True


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
