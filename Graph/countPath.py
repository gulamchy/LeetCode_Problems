def dfs(grid, r, c, visited):
    rowLength, colLength = len(grid), len(grid[0])

    if (min(r,c) < 0 or r == rowLength or c == colLength or (r,c) in visited or grid[r][c] == 1):
        return 0
    if r == rowLength - 1 and c == colLength - 1:
        return 1
    
    visited.add((r,c))

    count = 0 
    count += dfs(grid, r + 1, c, visited)
    count += dfs(grid, r - 1, c, visited)
    count += dfs(grid, r, c + 1, visited)
    count += dfs(grid, r, c - 1, visited)

    visited.remove((r,c))
    return count

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(dfs(grid,0,0,set()))