#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:len(arr)-1]),sum(arr[1:len(arr)]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
