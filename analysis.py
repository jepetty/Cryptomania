#! /usr/bin/env python3

import matplotlib.pyplot as plt

data = []

bucket = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '0': 0,
}

i = 0
with open('sample.txt') as f:
    for line in f:
        data.append((i, int(line)))
        i += 1

        bucket[line[:1]] += 1

print(bucket)

plt.scatter(*zip(*data))
plt.show()
