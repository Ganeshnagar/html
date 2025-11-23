graph = {
  1: [2, 3,4],
  2: [1,4, 5],
  3: [1,4],  
  5: [2,6,7],
  4: [1,2,3,7], 
  6: [5,7],
  7: [4,5,6],
 
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
bfs(visited, graph, 1, 7)
