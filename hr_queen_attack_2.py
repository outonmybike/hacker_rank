#!/bin/python3

import math
import os
import random
import re
import sys
import time 

#n 5 x 5 board size
#k  3 num of obs
#r_q 4 row of queen
#c_q 3 col of queen
#obs array of obs r,c
# 5 3 4 3 [[5, 5], [4, 2], [2, 3]]

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    r = r_q
    c = c_q
    m = r_q - c_q
    mp = r_q + c_q
    move_count = 0
    obs = []
    for x in range(k):
        if obstacles[x][0] == r_q or obstacles[x][1] == c_q or obstacles[x][0] - obstacles[x][1] == m or obstacles[x][0] + obstacles[x][1] == mp:
            obs.append(obstacles[x])

    # Horizontals right    
    pot_moves = []  
    for x in range(n):

        coord = []
        r = r_q
        c = x + 1 + c_q
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves,'hor right')
    move_count += len(pot_moves)

    # Horizontals left 
    pot_moves = []  
    for x in range(n):
        coord = []
        r = r_q
        c = c_q - 1 - x
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves,'hor left')
    move_count += len(pot_moves)

    # Verticals up    
    pot_moves = []  
    for x in range(n):
        coord = []
        c = c_q
        r = x + 1 + r_q
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves,'vert up')
    move_count += len(pot_moves)

    # Verticals down    
    pot_moves = []  
    for x in range(n):
        coord = []
        c = c_q
        r = r_q - 1 - x
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves,'vert down')
    move_count += len(pot_moves)

    #D up right
    pot_moves = []  
    for x in range(n):
        coord = []
        r = r_q + 1 + x
        c = c_q + 1 + x 
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves, 'diag up right')
    move_count += len(pot_moves)

    #D down right
    pot_moves = []  
    for x in range(n):
        coord = []
        r = r_q - 1 - x
        c = c_q + 1 + x 
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves, 'diag down right')
    move_count += len(pot_moves)

    #D up left
    pot_moves = []  
    for x in range(n):
        coord = []
        r = r_q + 1 + x
        c = c_q - 1 - x 
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves, 'diag up left')
    move_count += len(pot_moves)

    #D down left
    pot_moves = []  
    for x in range(n):
        coord = []
        r = r_q - 1 - x
        c = c_q - 1 - x 
        coord.append(r)
        coord.append(c)
        if coord in obs:
            break  
        if r > n or c > n or r < 1 or c < 1:
            break
        pot_moves.append(coord)
    # print(pot_moves, 'diag up left')
    move_count += len(pot_moves)

    # print(move_count)
    return move_count 


# [3,1], [3,7], [6,5]
start_time = time.time()
queensAttack(8,7,3,5,[[3,1], [3,7], [6,5], [5,3], [5,7], [2,4], [1,7]])
print("--- %s seconds ---" % (time.time() - start_time))

    