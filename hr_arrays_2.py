#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    removal_count_list = []
    unique_array = []
    for x in range(len(arr)):
        if arr[x] not in unique_array:
            unique_array.append(arr[x])


    for x in range(len(unique_array)):
        removals = 0
        for y in range(len(arr)):
            if unique_array[x] != arr[y]:
                removals += 1
        removal_count_list.append(removals)
    print(unique_array)
    print(removal_count_list)
    result = min(removal_count_list)
    print(result)
    return result 

equalizeArray([3,3,2,1,3])