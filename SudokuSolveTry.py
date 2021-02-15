import matplotlib.pyplot as plt

def drawGrid():
    for i in range(0,10):
        x = [0,9]
        y = [i,i]
        plt.plot(x,y,'b')
        x = [i,i]
        y = [0,9]
        plt.plot(x, y,'b')
def printNums(sud):
    step = 8
    for i in range(0,9):
        for j in range(0,9):
            plt.text(j+0.5,0.5+step,sud[i][j])
        step -= 1

def checkLine(sud,i):
    all = [1,2,3,4,5,6,7,8,9]
    for j in sud[i]:
        if j != 0:
            all.remove(j)
    return all
def checkColumn(sud,i):
    all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in sud:
        if j[i] != 0:
            all.remove(j[i])
    return all
def checkBox(sud,i,j):
    all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if i < 3:
        stepX = 0
    elif i > 5:
        stepX = 6
    else:
        stepX = 3
    if j < 3:
        stepY = 0
    elif j > 5:
        stepY = 6
    else:
        stepY= 3
    for n in range(0,3):
        for m in range(0,3):
            #print(n,m,sud[n + stepX][m + stepY])
            if sud[n + stepX][m + stepY] != 0:
                all.remove(sud[n + stepX][m+ stepY])
    return all

def checkAll(a,b,c):
    seeU = []
    for i in range(1, 10):
        if i in a and i in b and i in c:
            seeU.append(i)
    return seeU


sudoku = [ [5,0,0,0,1,0,0,0,4],
           [2,7,4,0,0,0,6,0,0],
           [0,8,0,9,0,4,0,0,0],
           [8,1,0,4,6,0,3,0,2],
           [0,0,2,0,3,0,1,0,0],
           [7,0,6,0,9,1,0,5,8],
           [0,0,0,5,0,3,0,1,0],
           [0,0,5,0,0,0,9,2,7],
           [1,0,0,0,2,0,0,0,3]]

sudoku = [ [5,3,0,0,7,0,0,0,0],
           [6,0,0,1,9,5,0,0,0],
           [0,9,8,0,0,0,0,6,0],
           [8,0,0,0,6,0,0,0,3],
           [4,0,0,8,0,3,0,0,1],
           [7,0,0,0,2,0,0,0,6],
           [0,6,0,0,0,0,2,8,0],
           [0,0,0,4,1,9,0,0,5],
           [0,0,0,0,8,0,0,7,9]]

sudoku = [ [1,9,0,0,3,0,0,0,8],
           [6,0,0,0,0,1,0,0,0],
           [0,0,2,5,0,0,0,0,3],
           [0,3,0,0,7,0,0,0,0],
           [0,0,0,0,4,3,0,0,0],
           [4,0,0,0,0,0,0,8,0],
           [0,0,9,0,0,0,0,5,0],
           [0,0,0,2,9,6,0,0,0],
           [0,0,8,0,0,0,0,2,7]]

for k in range(0,8):

    for i in range(0,9):
        for j in range(0,9):
            print(sudoku[i][j],i,j,checkAll(checkLine(sudoku,i), checkColumn(sudoku,j),checkBox(sudoku,i,j)))
            if len(checkAll(checkLine(sudoku,i), checkColumn(sudoku,j),checkBox(sudoku,i,j))) == 1 and sudoku[i][j] == 0:
                sudoku[i][j] = checkAll(checkLine(sudoku,i), checkColumn(sudoku,j),checkBox(sudoku,i,j))[0]

drawGrid()
printNums(sudoku)
plt.show()

