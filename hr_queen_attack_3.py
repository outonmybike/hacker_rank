#!/bin/python3

import math
import os
import random
import re
import sys
import time

#n 5 x 5 board size
#k  3 num of obstacles
#r_q 4 row of queen
#c_q 3 col of queen
#obstacles array of obs r,c
# 5 3 4 3 [[5, 5], [4, 2], [2, 3]]


# 3,3    [4,3],[4,4],[3,4],[2,4],[2,3],[2,2],[3,2],[4,2]



# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    r = r_q
    c = c_q
    m = r_q - c_q
    mp = r_q + c_q
    move_count = 0
    obs = []
    #get nearest obstacles
    for x in range(k):
        if obstacles[x][0] == r_q or obstacles[x][1] == c_q or obstacles[x][0] - obstacles[x][1] == m or obstacles[x][0] + obstacles[x][1] == mp:
            obs.append(obstacles[x])
    print(obs)


        # print(obstacles[x][0])
        # if obstacles[x]

    # all_moves = []
    # for x in range(n):
    #     coords_to_add = [[r+1+x,c],[r-1-x,c],[r+1+x,c+1+x],[r+x,c-1+x],[r+x,c+1+x],[r-1+x,c-1+x],[r-1+x,c],[r-1,c+1]]
    #     print(coords_to_add)
        

        




start_time = time.time()
queensAttack(8,7,3,5,[[3,1], [3,7], [6,5], [5,3], [5,7], [2,4], [1,7]])
print("--- %s seconds ---" % (time.time() - start_time))