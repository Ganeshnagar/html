graph = {
  1: [2, 3], 
  2: [4, 5], 
  3: [6,7],
  4: [8],
  5: [8],
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
