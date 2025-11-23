graph = {
  1: [2, 3], 
  2: [4], 
  3: [2],
  4: [6,5],
  5: [3,7],
  6: [], 
  7: [6]
} 

visited = set()

def dfs(visited, graph, node, goal):
    if node not in visited:
        print(node)
        visited.add(node)
        if node == goal:
            return True
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goal):
                return True
    return False

print("Path found by DFS:") 
dfs(visited, graph, 1, 7)

