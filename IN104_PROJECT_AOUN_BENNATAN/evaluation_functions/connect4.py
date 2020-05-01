from aiarena.connect4 import cell

def compter(joueur,gs):
    compt1 = 0
    if joueur == True :
        for i in range(7) :
            for j in range(6) :
                if gs.getCell(i,j).color == connect4.cell.WHITE :
                    #on test les lignes et colonnes
                    possible = True
                    if i<3 :
                        for u in range(1,4):
                            if gs.getCell(i+u,j).color == connect4.cell.BLACK : possible = False
                        if possible : compt1+=1
                        possible = True
                    if i>2:
                        for u in range(1,4):
                            if gs.getCell(i-u,j).color == connect4.cell.BLACK : possible = False
                        if possible : compt1+=1
                        possible = True
                    if j<4:
                        for u in range(1,4):
                            if gs.getCell(i,j+u).color == connect4.cell.BLACK : possible = False
                        if possible: compt1+=1
                        possible=True
                    if j>2:
                        for u in range(1,4):
                            if gs.getCell(i,j-u).color == connect4.cell.BLACK : possible = False
                        if possible: compt1+=1
                    
                    #on test les diagonales
    
    else:
        for i in range(7) :
            for j in range(6) :
                if gs.getCell(i,j).color == connect4.cell.BLACK :
                    #on test les lignes et colonnes
                    possible = True
                    if i<3 :
                        for u in range(1,4):
                            if gs.getCell(i+u,j).color == connect4.cell.WHITE : possible = False
                        if possible : compt1+=1
                        possible = True
                    if i>2:
                        for u in range(1,4):
                            if gs.getCell(i-u,j).color == connect4.cell.WHITE : possible = False
                        if possible : compt1+=1
                        possible = True
                    if j<4:
                        for u in range(1,4):
                            if gs.getCell(i,j+u).color == connect4.cell.WHITE : possible = False
                        if possible: compt1+=1
                        possible=True
                    if j>2:
                        for u in range(1,4):
                            if gs.getCell(i,j-u).color == connect4.cell.WHITE : possible = False
                        if possible: compt1+=1
    return compt1
                       
                    


def evaluate(gs):
    #on compte le nombre de puissance 4 possibles et on soustrait entre les joueurs
    compt1 = compter(True,gs)
    compt2 = compter(False,gs)
    return compt1-compt2
    raise NotImplementedError()
