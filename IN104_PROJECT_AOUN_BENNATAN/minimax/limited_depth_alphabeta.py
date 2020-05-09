#white is maximizing
#black is minimizing

import numpy as np

def minimax(node, maximize, get_children, evaluate, max_depth):
    if (max_depth == 0 or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        a = -(np.Inf)
        b = np.Inf
        for child in get_children(node):
            a = max(a,minimax(child,False,get_children,evaluate,max_depth-1))
            if a >= b:
                break
        return a

    elif (maximize == False):
        a = -(np.Inf)
        b = np.Inf
        for child in get_children(node):
            b = min(b,minimax(child,True,get_children,evaluate,max_depth-1))
            if a >= b:
                break
        return b