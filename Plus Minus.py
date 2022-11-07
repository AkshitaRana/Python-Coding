#HACKER RANK PROBLEM SOLVING QUESTION

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size=len(arr)
    negative,positive,zero=0,0,0
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zero+=1
    positiveProportion=format((positive/size),'.6f')
    negativeProportion=format((negative/size),'.6f')
    zeroProportion=format((zero/size),'.6f')    
    print(positiveProportion)
    print(negativeProportion)
    print(zeroProportion)    
             
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
