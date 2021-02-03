def efficientJanitor(weight):
    load_count = 0
    for x in range(len(weight)):
        for y in range(len(weight)):
            if x == y:
                continue
            elif (isinstance(weight[x], float) and isinstance(weight[y], float)):
                if weight[x] + weight[y] <= 3:
                    weight[x] = 'taken'
                    weight[y] = 'taken'
                    load_count += 1
                else:
                    weight[x] = 'taken'
                    load_count += 1
            else:
                continue
    print(load_count)
    return load_count

efficientJanitor([1.01, 1.99, 2.5, 1.01, 1.5])
