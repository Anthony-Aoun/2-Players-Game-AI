#white is maximizing
#black is minimizing

import numpy as np
import time

def alphabeta_transp(node, maximize, get_children, evaluate, maxTime,researchTime, a,b,table,coeff):
    tic = time.time()
    children = get_children(node)

    if (maxTime < researchTime or (children == [])):
        return evaluate(node)
    
    if (maximize == True):
        childrenNumber = len(children)
        for i,child in enumerate(children):
            elapsed = time.time() - tic
            #If the child has been visited we just take its value without exploring its children
            if child.toString() in table:
                value = table[child.toString()]
                a = max(a,value) 
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = alphabeta_transp(child, False, get_children, evaluate, coeff*(maxTime-elapsed)/(childrenNumber-i),researchTime,a,b,table,coeff)
                a = max(a,value)
                table.update({child.toString() : value})
            if a >= b:
                break
        return a

    elif (maximize == False):
        elapsed=0
        childrenNumber = len(children)
        for i,child in enumerate(children):
            elapsed = time.time() - tic
            #If the child has been visited we just take its value without exploring its children
            if child.toString() in table:
                value = table[child.toString()]
                b = min(b,value) 
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = alphabeta_transp(child, True, get_children, evaluate, coeff*(maxTime-elapsed)/(childrenNumber-i),researchTime,a,b,table,coeff)
                b = min(b,value)
                table.update({child.toString() : value})
            if a >= b:
                break
        return b

def minimax(node, maximize, get_children, evaluate, maxTime,researchTime,coeff):
    return alphabeta_transp(node, maximize, get_children, evaluate, maxTime, researchTime,-(np.Inf),np.Inf,{},coeff)


