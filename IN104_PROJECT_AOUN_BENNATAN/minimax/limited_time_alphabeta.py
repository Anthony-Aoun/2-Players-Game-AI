#white is maximizing
#black is minimizing

import numpy as np
import time

def alphabeta(node, maximize, get_children, evaluate, maxTime,researchTime, a,b):
    tic = time.time()
    children = get_children(node)

    if (maxTime < researchTime or (children == [])):
        return evaluate(node)
    
    if (maximize == True):
        childrenNumber = len(children)
        for i,child in enumerate(children):
            elapsed = time.time() - tic
            a = max(a,alphabeta(child, False, get_children, evaluate, (maxTime-elapsed)/(childrenNumber-i),researchTime,a,b))
            if a >= b:
                break
        return a

    elif (maximize == False):
        childrenNumber = len(children)
        for i,child in enumerate(children):
            elapsed = time.time() - tic
            b = min(b,alphabeta(child, True, get_children, evaluate, (maxTime-elapsed)/(childrenNumber-i),researchTime,a,b))
            if a >= b:
                break
        return b

def minimax(node, maximize, get_children, evaluate, maxTime, researchTime):
    return alphabeta(node, maximize, get_children, evaluate, maxTime, researchTime, -(np.Inf),np.Inf)


