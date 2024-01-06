# Recursive 
graph = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
]
def recursiveDFS(row, col, graph, visited=set()):
    pos = (row, col)
    if pos in visited:
        return
    if(row < 0 or row >= len(graph) or col < 0 or col >= len(graph[row])):
        return
    if graph[row][col] == 0:
        return
    
    visited.add(pos)
    print(pos)

    recursiveDFS(row - 1 , col, graph, visited)
    recursiveDFS(row + 1, col, graph, visited)
    recursiveDFS(row, col - 1, graph, visited)
    recursiveDFS(row, col + 1, graph, visited)

recursiveDFS(3, 3, graph)


# Iterative Stack

def iterativeDFS(start, graph):
    stack = [start]
    visited = {start}

    while stack:
        pos = stack.pop()

        print(pos)

        for nei in getNeighbors(pos, graph):
            if nei not in visited:
                visited.add(nei)
                stack.append(nei)

def getNeighbors(pos, graph):
    row, col = pos

    neighbors = (
        (row -1, col),
        (row + 1, col),
        (row, col -1),
        (row, col + 1),
    )

    def isValid(pos):
        r,c = pos
        return (r >= 0 and r < len(graph) and c >= 0 and c < len(graph[r]) and graph[r][c] == 1)
    
    return [pos for pos in neighbors if isValid(pos)]

iterativeDFS((3,3), graph)