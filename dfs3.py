graph = {
  1: [2,3,4],
  2: [1,4,5], 
  3: [1,4],
  4: [1,2,3,7],
  5: [2,6,7], 
  6: [5,7],
  7: [4,5,6]
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
dfs(visited, graph, 2, 7)
