def jumpingOnClouds(c):
    c.append(0)
    jumps = 0
    position = 0
    skipped = []
    for x in range(len(c)-2):
        if position >= len(c):
            break
        elif skipped.count(x) > 0:
            continue 
        elif c[x+2] == 0:
            position += 2
            jumps += 1
            skipped.append(x+1)
        else:
             position += 1
             jumps += 1
    return jumps
    #     print(jumps, 'jumps')
    #     print(position, 'position')
    # print(jumps)
    # print(position)

jumpingOnClouds([0, 0, 0, 0, 1, 0])