#!/usr/bin/env python3

# Author: Rahul Akshaykumar Shah
# Author ID: 125503227
# Date Created: 2024/06/05

import sys

if len(sys.argv) != 2:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1

print("blast off!")