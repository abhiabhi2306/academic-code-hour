#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    lastcloud = len(c)-1
    lastsecond = len(c)-2
    position = 0
    count = 0
    
    while position<lastsecond:
        if c[position+2]==0:
            position+=2
        else:
            position+=1
        count+=1
        
    if position!=lastcloud:
        count+=1
            
    return count
        

                
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
