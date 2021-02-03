import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    valley_count = 0
    str = list(path)
    position = [0]
    for x in range(steps):
        if str[x] == 'D':
            position.append((position[x])-1)
        else:
            position.append((position[x]+1))
    print(position)
    for x in range(steps):
        if (position[x] == 0 and position[x+1] == -1):
            valley_count += 1
    print(valley_count)




countingValleys(100,'DDUDUDDUDDUDDUUUUDUDDDUUDDUUDDDUUDDUUUUUUDUDDDDUDDUUDUUDUDUUUDUUUUUDDUDDDDUDDUDDDDUUUUDUUDUUDUUDUDDD')