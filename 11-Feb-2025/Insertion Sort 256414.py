# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, len(arr)):
        index = i
        for j in range(i - 1, -1, -1):
            if arr[index] < arr[j]:
                cont_temp = arr[index]
                arr[index] = arr[j]
                print(" ".join((list(map(str, arr)))))
                arr[j] = cont_temp
                index = j
    print(" ".join((list(map(str, arr)))))
    
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
