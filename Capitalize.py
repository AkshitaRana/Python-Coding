# PYTHON HACKER RANK QUESTION

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    cap_str = s.split(" ")
    name = []
    for i in cap_str:
        name.append(i.capitalize())
    return " ".join(name)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
