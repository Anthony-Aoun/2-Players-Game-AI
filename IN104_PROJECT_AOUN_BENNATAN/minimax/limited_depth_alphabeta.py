#white is maximizing
#black is minimizing

import numpy as np

def alphabeta(node, maximize, get_children, evaluate, max_depth,a,b):
    if (max_depth == 0 or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        for child in get_children(node):
            a = max(a,alphabeta(child,False,get_children,evaluate,max_depth-1,a,b))
            if a >= b:
                break
        return a

    elif (maximize == False):
        for child in get_children(node):
            b = min(b,alphabeta(child,True,get_children,evaluate,max_depth-1,a,b))
            if a >= b:
                break
        return b

def minimax(node, maximize, get_children, evaluate, max_depth):
    return alphabeta(node, maximize, get_children, evaluate, max_depth,-(np.Inf),np.Inf)