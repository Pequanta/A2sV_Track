# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    num_swaps = 0
    for i in range(len(a)):
        for j in range(1, len(a) - i):
            if a[j - 1] > a[j]:
                num_swaps += 1
                a[j - 1], a[j] = a[j] , a[j - 1]
    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
