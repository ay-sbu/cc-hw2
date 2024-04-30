p = 23
for i in range(1, p): # [1, p-1]
    visited = [False] * p
    trace = []
    k = 1
    counter = 0
    while True:
        if counter == p-1:
            break
        if visited[k] == True:
            break
        visited[k] = True
        k = (k * i) % p
        if k == 0:
            break
        counter += 1
        trace.append(k)
    if counter == p-1:
        print('generator: ', i)
        print(trace)
        break

