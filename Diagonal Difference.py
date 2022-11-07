#HACKER RANK PROBLEM SOLVING QUESTION

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    # Write your code here
    sum1,sum2=0,0
    for i in range(n):
        for j in range(i,n):
            sum1+=arr[i][j]
            break
    for i in range(n):
        for j in range(n-(i+1),-1,-1):
            sum2+=arr[i][j]
            break
    return abs(sum1-sum2)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
