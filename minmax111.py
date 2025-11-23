import math
def minimax(depth, nodeIndex, maximizingPlayer, values, targetDepth):
    if depth == targetDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -math.inf
        for i in range(2):  # Two children for each node
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, targetDepth)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2):  # Two children for each node
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, targetDepth)
            best = min(best, val)
        return best
if __name__ == "__main__":
    values = [10, 9, 14, 18, 5, 4, 50, 3]  # Leaf node values
    print("The optimal value is:", minimax(0, 0, True, values, 3))
