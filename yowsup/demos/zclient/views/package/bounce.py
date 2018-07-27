def bounce(height):
    height = int(height)
    grid = []

    for i in range(height + 1):
        grid.append(list())
        
    max = height
    min = 0
    step = 1
    count = 0
    q = ""

    while max != min:
        for i in range(min, max + 1, step):
            count+=1
            for j in range(count - 1):
                if len(grid[i]) < j + 1:
                    grid[i].append(0)      
            grid[i].append(1)
        temp = min
        min = max - 1 if temp < max else max + 1
        max = temp  if temp < max else temp + 1
        step*=-1
        
    longest = None
    if len(grid) > 1:
        longest = len(grid[-1])
    else:
        longest = 1

    for row in grid:
        for i in range(longest - len(row)):
            row.append(0)

    for row in grid:
        for i in row:
            if i == 1:
                q += "O"
            else:
                q += "_"
        q += "\n"
    return q
