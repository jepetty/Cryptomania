#! /usr/bin/env python3

import matplotlib.pyplot as plt

data_full = []
data_trunc = []

bucket_full = {
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

bucket_trunc = {
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
        data_full.append((i, int(line)))
        data_trunc.append((i, int(line[1:])))

        bucket_full[line[:1]] += 1
        bucket_trunc[line[1:2]] += 1

        i += 1

print(bucket_full)
print(bucket_trunc)

plt.scatter(*zip(*data_full))
plt.show()

plt.scatter(*zip(*data_trunc))
plt.show()
