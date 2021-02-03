def hourglassSum(arr):
    hg_w = 3
    hg_h = 3
    col_count = len(arr[0])
    row_count = len(arr)
    hg_hor = col_count - (hg_w -1)
    hg_vert = row_count - (hg_h -1)
    hg_count = hg_hor * hg_vert 
    sum_list = []
    for x in range(hg_hor):
        for y in range(hg_vert):
            hg_sum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            sum_list.append(hg_sum)
    print(sum_list)
    print(max(sum_list))


    # print(row_count, 'rows')
    # print(hour_glasses_hor)
    # print(hour_glasses_vert)
    # print(col_count)
    # print(arr)
    # print(arr[0][0])



hourglassSum([[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]])






# [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]