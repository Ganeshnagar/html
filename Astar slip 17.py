import heapq

graph = {
    'A': [('B', 9), ('C', 4),('D',7)],
    'B': [('E', 11)],
    'C': [('E', 17),('F',12)],
    'D': [('F', 14)],
    'E': [('G', 5)],
    'F': [('G',9)],
    'G':[]
}

h = {'A': 21, 'B': 14, 'C': 18, 'D': 18, 'E': 5, 'F': 8 ,'G':0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        for neigh, cost in graph[node]:
            g2 = g + cost
            f2 = g2 + h[neigh]
            heapq.heappush(pq, (f2, g2, neigh, path + [neigh]))

# Run
path, cost = astar('A', 'G')
print("Path:", path, " Cost:", cost)
