#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    new_list = []
    l = len(a)
    a = a + a
    for x in range(l):
        new_list.append(a[x+d])
    return new_list

rotLeft([1, 2, 3, 4, 5],4)         