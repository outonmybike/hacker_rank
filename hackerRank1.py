import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    match_count = 0
    o_ar = ar
    for x in range(n):
        for y in range(n):
            if o_ar[x] == o_ar[y]:
                if x == y:
                    continue
                o_ar[x] = 'match'
                o_ar[y] = 'match'
    for x in range(len(o_ar)):
        if o_ar[x] == 'match':
            match_count += 1
    match = int(match_count/2)
    return match





sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])





# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
