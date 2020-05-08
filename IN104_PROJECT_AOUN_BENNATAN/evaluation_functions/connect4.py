import aiarena

def count(player,gs):
    nb=0
    if player == 'w':
        for i in range(6):
            for j in range(7):
                if gs.getCell(i,j).color == aiarena.connect4.cell.NONE:
                    #Vertical
                    inRow=1

                    up=1
                    while ((i+up)<6 and gs.getCell(i+up,j).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        up+=1
                    down=1
                    while ((i-down)>=0 and gs.getCell(i-down,j).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        down+=1

                    if (inRow >= 4):
                        nb+=1

                    #Horizontal
                    inRow=1

                    right=1
                    while ((j+right)<7 and gs.getCell(i,j+right).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        right+=1
                    left=1
                    while ((j-left)>=0 and gs.getCell(i,j-left).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        left+=1

                    if (inRow >= 4):
                        nb+=1

                    #First Diagonal
                    inRow=1

                    right=1
                    while ((i+right)<6 and (j+right)<7 and gs.getCell(i+right,j+right).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        right+=1
                    left=1
                    while ((i-left)>=0 and (j-left)>=0 and gs.getCell(i-left,j-left).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        left+=1
                    
                    if (inRow >= 4):
                        nb+=1

                    #Second Diagonal
                    inRow=1

                    right=1
                    while ((i-right)>=0 and (j+right)<7 and gs.getCell(i-right,j+right).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        right+=1
                    left=1
                    while ((i+left)<6 and (j-left)>=0 and gs.getCell(i+left,j-left).color == aiarena.connect4.cell.WHITE):
                        inRow+=1
                        left+=1
                    
                    if (inRow >= 4):
                        nb+=1

    else:
        for i in range(6):
            for j in range(7):
                if gs.getCell(i,j).color == aiarena.connect4.cell.NONE:
                    #Vertical
                    inRow=1

                    up=1
                    while ((i+up)<6 and gs.getCell(i+up,j).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        up+=1
                    down=1
                    while ((i-down)>=0 and gs.getCell(i-down,j).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        down+=1

                    if (inRow >= 4):
                        nb+=1

                    #Horizontal
                    inRow=1

                    right=1
                    while ((j+right)<7 and gs.getCell(i,j+right).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        right+=1
                    left=1
                    while ((j-left)>=0 and gs.getCell(i,j-left).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        left+=1

                    if (inRow >= 4):
                        nb+=1

                    #First Diagonal
                    inRow=1

                    right=1
                    while ((i+right)<6 and (j+right)<7 and gs.getCell(i+right,j+right).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        right+=1
                    left=1
                    while ((i-left)>=0 and (j-left)>=0 and gs.getCell(i-left,j-left).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        left+=1
                    
                    if (inRow >= 4):
                        nb+=1

                    #Second Diagonal
                    inRow=1

                    right=1
                    while ((i-right)>=0 and (j+right)<7 and gs.getCell(i-right,j+right).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        right+=1
                    left=1
                    while ((i+left)<6 and (j-left)>=0 and gs.getCell(i+left,j-left).color == aiarena.connect4.cell.BLACK):
                        inRow+=1
                        left+=1
                    
                    if (inRow >= 4):
                        nb+=1

    return nb


def evaluate(gs):
    #on compte le nombre de puissance 4 possibles et on soustrait entre les joueurs
    nb1 = count('w',gs)
    nb2 = count('b',gs)
    return nb1-nb2

'''
Cette evaluation a un grand defaut. L'IA cherche a alligner
ses pieces sans m'empecher d'alligner les miennes.

Exemple:
o:moi
x:IA



      x
ooo   x  AI'turn

L'IA va faire le choix suivant et me laisse gagner: 


      x
      x
ooo   x  Human'turn

Ce n'est pas sa faute, selon son raisonnement, de cette maniere
il minimise la difference de possibilites de gain (l'annule dans
ce cas)

Il faut ajouter une codition du style: si ton adversaire a 3 pieces 
allignees et que tu peux les bloquer vas-y

'''







