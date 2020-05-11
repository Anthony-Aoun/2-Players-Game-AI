#white is maximizing
#black is minimizing

#table is a dictionnary {state : score}

import numpy as np

def transposition(node, maximize, get_children, evaluate, max_depth,table):
    if (max_depth == 0 or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        best = -(np.Inf)
        for child in get_children(node):
            #If the child has been visited we just take its value without exploring its children
            if child in table:
                value = table[child]
                best = max(best,value)             
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = minimax(child, False, get_children, evaluate, max_depth-1)
                table.update({child : value})
                best = max(best, value)
        return best

    elif (maximize == False):
        best = np.Inf
        for child in get_children(node):
            #If the child has been visited we just take its value without exploring its children
            if child in table:
                value = table[child]
                best = max(best,value)
            #If the child hasn't been visited, we visit it and add it to table
            else:
                value = minimax(child, True, get_children, evaluate, max_depth-1)
                table.update({child : value})
                best = min(best, value)      
        return best

def minimax(node, maximize, get_children, evaluate, max_depth):
    return transposition(node, maximize, get_children, evaluate, max_depth,{})