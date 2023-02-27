#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    count = 0
    for i in range(len(A)):
        tempCount=0
        for j in range(len(B)):
            if(A[i]+B[j]>=k):
                tempCount=1
                B[j]=0
                break
        
        if tempCount:
            count+=1
        else:
            break
    
    if count==len(A):
        print("YES")
    else:
        print("NO")    
    
        

    # Write your code here

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

