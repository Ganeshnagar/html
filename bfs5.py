graph = {
  1: [2, 4], 
  2: [3],
  3: [4,5,6], 
  4: [2],
  5: [7,8],
  6: [8],
  7: [8],
  8: []
}

visited = [] 

def bfs(visited, graph, node, goal):
    queue = []
    queue.append(node)

    while queue:
        s = queue.pop(0)
        if s not in visited:
            visited.append(s)
            print(s)
            if s == goal:
                return True
            for neighbour in graph[s]:
                queue.append(neighbour)

    return False

print("Path found by BFS:")
bfs(visited, graph, 1, 8)
