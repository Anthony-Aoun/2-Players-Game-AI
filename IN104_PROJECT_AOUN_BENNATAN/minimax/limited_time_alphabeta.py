#white is maximizing
#black is minimizing

import numpy as np
import time

def alphabeta(node, maximize, get_children, evaluate, maxTime,researchTime, a,b):
    if (maxTime < researchTime or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        elapsed=0
        childNumber = len(get_children(node))
        for i,child in enumerate(get_children(node)):
            tic = time.time()
            a = max(a,alphabeta(child, False, get_children, evaluate, (maxTime-elapsed)/(childNumber-i),researchTime,a,b))
            if a >= b:
                break
            elapsed += time.time() - tic
        return a

    elif (maximize == False):
        elapsed=0
        childNumber = len(get_children(node))
        for i,child in enumerate(get_children(node)):
            tic = time.time()
            b = min(b,alphabeta(child, True, get_children, evaluate, (maxTime-elapsed)/(childNumber-i),researchTime,a,b))
            if a >= b:
                break
            elapsed+= time.time() - tic
        return b

def minimax(node, maximize, get_children, evaluate, maxTime, researchTime):
    return alphabeta(node, maximize, get_children, evaluate, maxTime, researchTime, -(np.Inf),np.Inf)


