#white is maximizing
#black is minimizing

import numpy as np

def nega(node, maximize, get_children, evaluate, max_depth, a, b):
    if (max_depth == 0 or (get_children(node) == [])):
        if maximize:
            return evaluate(node)
        else:
            return -evaluate(node)

    for i,child in enumerate(get_children(node)):
        if i!=0:
            score = -nega(child,not(maximize),get_children,evaluate,max_depth-1,-a-1,-a)

            if a<score and score<b:
                score = -nega(child,not(maximize),get_children,evaluate,max_depth-1,-b,-score)

        else:
            score = -nega(child,not(maximize),get_children,evaluate,max_depth-1,-b,-a)

        a = max(a,score)

        if a >= b:
            break

    return a

def minimax(node, maximize, get_children, evaluate, max_depth):
    return nega(node, maximize, get_children, evaluate, max_depth, -(np.Inf), np.Inf)

    

