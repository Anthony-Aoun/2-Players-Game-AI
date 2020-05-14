#white is maximizing
#black is minimizing

import numpy as np
import time

def nega_transp(node, maximize, get_children, evaluate, maxTime, researchTime, a, b, table):
    if (maxTime < researchTime or (get_children(node) == [])):
        if maximize:
            return evaluate(node)
        else:
            return -evaluate(node)

    elapsed=0
    childNumber = len(get_children(node))
    for i,child in enumerate(get_children(node)):
        tic = time.time()

        #If the child has been visited we just take its value without exploring its children
        if child.toString() in table:
            score = table[child.toString()]

        #If the child hasn't been visited, we visit it and add it to table
        else:
            if i!=0:
                score = -nega_transp(child,not(maximize),get_children,evaluate,(maxTime-elapsed)/(childNumber-i),researchTime,-a-1,-a,table)

                if a<score and score<b:
                    score = -nega_transp(child,not(maximize),get_children,evaluate,(maxTime-elapsed)/(childNumber-i),researchTime,-b,-score,table)

            else:
                score = -nega_transp(child,not(maximize),get_children,evaluate,(maxTime-elapsed)/(childNumber-i),researchTime,-b,-a,table)

            table.update({child.toString() : score})

        a = max(a,score)

        if a >= b:
            break
        
        elapsed += time.time() - tic

    return a

def minimax(node, maximize, get_children, evaluate, maxTime, researchTime):
    return nega_transp(node, maximize, get_children, evaluate, maxTime, researchTime, -(np.Inf), np.Inf,{})

    

