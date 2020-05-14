#white is maximizing
#black is minimizing

import numpy as np
import time

def alphabeta_transp(node, maximize, get_children, evaluate, maxTime,researchTime, a,b,table):
    if (maxTime < researchTime or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        elapsed=0
        childNumber = len(get_children(node))
        for i,child in enumerate(get_children(node)):
            tic = time.time()
            #If the child has been visited we just take its value without exploring its children
            if child.toString() in table:
                value = table[child.toString()]
                a = max(a,value) 
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = alphabeta_transp(child, False, get_children, evaluate, (maxTime-elapsed)/(childNumber-i),researchTime,a,b,table)
                a = max(a,value)
                table.update({child.toString() : value})
            if a >= b:
                break
            elapsed += time.time() - tic
        return a

    elif (maximize == False):
        elapsed=0
        childNumber = len(get_children(node))
        for i,child in enumerate(get_children(node)):
            tic = time.time()
            #If the child has been visited we just take its value without exploring its children
            if child.toString() in table:
                value = table[child.toString()]
                b = min(b,value) 
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = alphabeta_transp(child, True, get_children, evaluate, (maxTime-elapsed)/(childNumber-i),researchTime,a,b,table)
                b = min(b,value)
                table.update({child.toString() : value})
            if a >= b:
                break
            elapsed+= time.time() - tic
        return b

def minimax(node, maximize, get_children, evaluate, maxTime,researchTime):
    return alphabeta_transp(node, maximize, get_children, evaluate, maxTime, researchTime,-(np.Inf),np.Inf,{})


