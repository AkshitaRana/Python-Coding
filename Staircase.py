#!/bin/python3
#Python hacker rank question

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    x='#'
    for i in range(n):
        print((x*(i+1)).rjust(n))
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
