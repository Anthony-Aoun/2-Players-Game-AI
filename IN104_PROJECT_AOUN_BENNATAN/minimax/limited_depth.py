#white is maximizing
#black is minimizing

import numpy as np

def minimax(node, maximize, get_children, evaluate, max_depth):
    if (max_depth == 0 or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        best = -(np.Inf)
        for child in get_children(node):
            value = minimax(child, False, get_children, evaluate, max_depth-1)
            best = max(best, value)
        return best

    elif (maximize == False):
        best = np.Inf
        for child in get_children(node):
            value = minimax(child, True, get_children, evaluate, max_depth-1)
            best = min(best, value)
        return best


    

