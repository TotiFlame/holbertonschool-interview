#!/usr/bin/python3
""" task 0 """


def canUnlockAll(boxes):
    """ method """
    n = len(boxes)
    opened_boxes = [0]
    lock_boxes = []
    keys = boxes[0]
    for i in range(1, n):
            if i in opened_boxes:
                continue
            if i in keys:
                opened_boxes.append(i)
                keys += boxes[i]
                keys = list(set(keys))
            else:
                lock_boxes.append(i)
    for j in lock_boxes:
        if j in keys:
            opened_boxes.append(j)
            keys += boxes[j]
            keys = list(set(keys))
    if len(opened_boxes) == n:
        return True
    else:
        return False
