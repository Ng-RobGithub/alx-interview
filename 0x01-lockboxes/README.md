=========================0x01-lockboxes========================

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

# Box Unlocker

This Python module determines if all boxes in a list of lists can be opened.

## Usage

To use this module, call the `can_unlock_all()` function with a list of lists containing keys in each box.

```python
boxes = [    [1, 3],
    [2],
    [3, 0],
    [1, 2, 3],
]
print(can_unlock_all(boxes))
