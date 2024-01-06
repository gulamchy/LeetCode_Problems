from collections import deque
def bfs(grid):
    rowLength, colLength = len(grid), len(grid[0])
    visited = set()
    queue = deque()
    queue.append((0,0))
    visited.add((0,0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == rowLength - 1 and c == colLength - 1:
                return length
            
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if(min(r + dr, c + dc) < 0 or r + dr == rowLength or c + dc == colLength or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visited.add((r + dr, c + dc))
        length += 1

# Example of Implementation
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

print(bfs(grid))