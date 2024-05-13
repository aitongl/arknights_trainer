import random

def generate():
    generateMap(5, 5)

def generateMap(r, c):
    startNode = (random.randint(0, r-1), c-1)
    connectedNodes = []
    board = generateBoard(5, 5)
    startX, startY = startNode
    connectedNodes = findPath(startX, startY, connectedNodes, board)
    print(connectedNodes)

def findPath(r, c, connections, board):
    if c == 0:
        return connections
    else:
        L = [, (-1, 0), (0, 1), (0, -1)]
        random.shuffle(L)
        for changeX, changeY in L:
            if isLegal(r, c, changeX, changeY, connections, board):
                connections.append([(r,c), (r+changeY, c+changeX)])
                res = findPath(r+changeY, c+changeX, connections, board)
                if res != None:
                    return connections
                else:
                    connections.pop() 
        return None
    
def isLegal(r, c, changeX, changeY, connections, board):
    if r+changeY < 0 or r+changeY >= len(board):
        return False
    if c+changeX < 0 or c+changeX >= len(board[0]):
        return False
    for node1, node2 in connections:
        if (r+changeY, c+changeX) == node1 or (r+changeY, c+changeX)  == node2:
            return False
    return True
                
    
# creates an empty board that avoids aliasing
def generateBoard(rows, cols):
    board = []
    for i in range(rows):
        newRow = []
        for j in range(cols):
            newRow.append(None)
        board.append(newRow)
    return board

generate()