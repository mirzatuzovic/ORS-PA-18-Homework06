#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            alice += 1
        if a[i] < b[i]:
            bob += 1
        if a[i] == b[i]:
            pass
        i += 1

    return alice, bob


if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()