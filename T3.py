#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n > 100:
        quit

    for i in range(1, n+1):
        str_for_print = (n-i) * " " + i * "#"
        print(str_for_print)

if _name_ == '_main_':
    n = int(input())

    staircase(n)