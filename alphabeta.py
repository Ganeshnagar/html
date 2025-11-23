import math
def alphabeta(depth, nodeIndex, alpha, beta, maximizingPlayer, values, targetDepth):
    if depth == targetDepth:
        return values[nodeIndex]
    if maximizingPlayer:   
        best = -math.inf
        for i in range(0, 2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, 
                            alpha, beta, False, values, targetDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning 
            if beta <= alpha:
                break
        return best
    else:  
        best = math.inf    
        for i in range(0, 2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,  
                            alpha, beta, True, values, targetDepth)            
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
if __name__=="__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  
    print("The optimal value is :", alphabeta(0, 0, -math.inf, math.inf, True, values, 3))
