#white is maximizing
#black is minimizing

import numpy as np

def nega_transp(node, maximize, get_children, evaluate, max_depth, a, b, table):
    if (max_depth == 0 or (get_children(node) == [])):
        if maximize:
            return evaluate(node)
        else:
            return -evaluate(node)

    for i,child in enumerate(get_children(node)):
        #If the child has been visited we just take its value without exploring its children
        if child.toString() in table:
            score = table[child.toString()]

        #If the child hasn't been visited, we visit it and add it to table
        else:
            if i!=0:
                score = -nega_transp(child,not(maximize),get_children,evaluate,max_depth-1,-a-1,-a,table)

                if a<score and score<b:
                    score = -nega_transp(child,not(maximize),get_children,evaluate,max_depth-1,-b,-score,table)

            else:
                score = -nega_transp(child,not(maximize),get_children,evaluate,max_depth-1,-b,-a,table)

            table.update({child.toString() : score})

        a = max(a,score)

        if a >= b:
            break

    return a

def minimax(node, maximize, get_children, evaluate, max_depth):
    return nega_transp(node, maximize, get_children, evaluate, max_depth, -(np.Inf), np.Inf,{})

    

