import math

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        bestVal = -math.inf
        for i in range(0, 2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,  
                          False, values, alpha, beta)
            bestVal = max(bestVal, val)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal
    else: 
        bestVal = math.inf
        for i in range(0, 2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,  
                          True, values, alpha, beta)
            bestVal = min(bestVal, val) 
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal
if __name__=="__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  
    print("The optimal value is:", alphabeta(0, 0, True, values, -math.inf, math.inf))
