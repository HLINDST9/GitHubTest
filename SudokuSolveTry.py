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

numGrid = [[5,0,0,0,1,0,0,0,4],
           [2,7,4,0,0,0,6,0,0],
           [0,8,0,9,0,4,0,0,0],
           [8,1,0,4,6,0,3,0,2],
           [0,0,2,0,3,0,1,0,0],
           [7,0,6,0,9,1,0,5,8],
           [0,0,0,5,0,3,0,1,0],
           [0,0,5,0,0,0,9,2,7],
           [1,0,0,0,2,0,0,0,3]]

drawGrid()

printNums(numGrid)
plt.show()