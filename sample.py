#! /usr/bin/env python3

import random
import string

n = 100
values = []
collisions = []
avg = 0

j = 0
while j < n:
    s = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits
        + string.ascii_lowercase) for _ in range(8))

    # ascii value of the input string
    val = ''.join(str(ord(c)) for c in s)

    iterations = 0
    while iterations < 10:
        i = 0
        # mod by length of document to avoid going out of bounds
        val = int(val) % 499999
        with open('lorenz.txt') as f:
            for line in f:
                # print the result at the proper index
                if (i == val):
                    val = line[:-5].replace('.', '')
                i += 1
        iterations += 1

    if val not in values:
        values.append(val)
    else:
        collisions.append(val)

    avg = avg + (int(val) * 1 / n+1)

    j += 1

print(collisions)
print(len(collisions))
print(avg)

with open('sample.txt', 'w') as f:
    for val in values:
        f.write(val + '\n')
