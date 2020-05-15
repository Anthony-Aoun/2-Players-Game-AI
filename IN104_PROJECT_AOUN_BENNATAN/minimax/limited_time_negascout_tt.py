#white is maximizing
#black is minimizing

import numpy as np
import time

def nega_transp(node, maximize, get_children, evaluate, maxTime, researchTime, a, b, table):
    tic = time.time()
    children = get_children(node)

    if (maxTime < researchTime or (children == [])):
        if maximize:
            return evaluate(node)
        else:
            return -evaluate(node)

    childrenNumber = len(children)
    for i,child in enumerate(children):
        #If the child has been visited we just take its value without exploring its children
        if child.toString() in table:
            score = table[child.toString()]

        #If the child hasn't been visited, we visit it and add it to table
        else:
            
            if i!=0:
                elapsed = time.time()-tic
                score = -nega_transp(child,not(maximize),get_children,evaluate,(maxTime-elapsed)/(childrenNumber-i),researchTime,-a-1,-a,table)

                if a<score and score<b:
                    elapsed = time.time()-tic
                    score = -nega_transp(child,not(maximize),get_children,evaluate,(maxTime-elapsed)/(childrenNumber-i),researchTime,-b,-score,table)

            else:
                elapsed = time.time()-tic
                score = -nega_transp(child,not(maximize),get_children,evaluate,(maxTime-elapsed)/(childrenNumber-i),researchTime,-b,-a,table)

            table.update({child.toString() : score})

        a = max(a,score)

        if a >= b:
            break

    return a

def minimax(node, maximize, get_children, evaluate, maxTime, researchTime):
    return nega_transp(node, maximize, get_children, evaluate, maxTime, researchTime, -(np.Inf), np.Inf,{})

    

