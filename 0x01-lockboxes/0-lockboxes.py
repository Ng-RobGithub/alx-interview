#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set(boxes[0])
    unlocked = set([0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            keys.update(boxes[key])
            unlocked.add(key)

    return len(unlocked) == len(boxes)
