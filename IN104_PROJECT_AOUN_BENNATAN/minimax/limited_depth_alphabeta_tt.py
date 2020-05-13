#white is maximizing
#black is minimizing

#table is a dictionnary {state : score}

import numpy as np

def alphabeta_transp(node, maximize, get_children, evaluate, max_depth,a,b,table):
    if (max_depth == 0 or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        for child in get_children(node):
            #If the child has been visited we just take its value without exploring its children
            if child.toString() in table:
                value = table[child.toString()]
                a = max(a,value)             
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = alphabeta_transp(child, False, get_children, evaluate, max_depth-1,a,b,table)
                a = max(a,value)
                table.update({child.toString() : value})
            if a >= b:
                break
        return a

    elif (maximize == False):
        for child in get_children(node):
            #If the child has been visited we just take its value without exploring its children
            if child.toString() in table:
                value = table[child.toString()]
                b = min(b,value)
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = alphabeta_transp(child, True, get_children, evaluate, max_depth-1,a,b,table)
                b = min(b,value)
                table.update({child.toString() : value})
            if a >= b:
                break    
        return b

def minimax(node, maximize, get_children, evaluate, max_depth):
    return alphabeta_transp(node, maximize, get_children, evaluate, max_depth,-(np.Inf), np.Inf, {})