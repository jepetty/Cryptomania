#! /usr/bin/env python3

import sys

# error if no input
if (len(sys.argv) < 2):
    print('Usage:')
    print('  python3 hash.py \'hello world\'')
    sys.exit(0)

# get user input
s = sys.argv[1]

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

print(val)
