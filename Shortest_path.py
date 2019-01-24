"""
The idea to implement this code is to do breadth first search
since it is 8*8 matrix,  we can implement it via queue or using recursion.
I will try to implement it with recursion.
Basic technique :
if you are at (i,j) :
Then:
up =(i-1,j)
down=(i+1,j)
left=(i,j-1)
right=(i,j+1)

With the above strategy, we will implement this intuitive puzzle.
We will take two array, one with update of visited cells already and other with the original values
@Author - Mayank Yadav
"""
import numpy as np


n=8
visited=np.zeros((n,n),np.int32)
minDist=65535 #A rough int max
dist=0 #to keep into account the actual distance and as a counter

#making function to check whether i and j are within bounds of chess board

def boundary(i,j):

    if(i<n and j<n and i>=0 and j>=0):
        return True
    else:
        return False

#check if the cell is already visited, if it is already visited then it will be 1 in visited numpy array.
#with that approach if it is zero in original or visited , then the function will return fals

def visit(chess,i,j):

    if(chess[i][j]==0 or visited[i][j]==1):
        return False
    return True

#Recursive function to find the distance
#We are taking into account that it will always start from [0,0] and want to reach [7,7]

def shortestPath(chess,dist,i=0,j=0):
    #checking if it already reached the final cell
    global visited
    global minDist
    if(i==(n-1) and j==(n-1)):
        minDist=min(dist,minDist)
        return
    #Current cell is already visited now
    visited[i][j]=1
    #print(visited[i][j])

    #now checking for up, down, left, right
    #UP
    if(boundary(i-1,j) and visit(chess,i-1,j)):
        shortestPath(chess,dist+1,i-1,j)

    # DOWN
    if (boundary(i+1,j) and visit(chess,i+1,j)):
        shortestPath(chess,dist+1,i+1,j)

    # LEFT
    if (boundary(i,j-1) and visit(chess,i,j-1)):
        shortestPath(chess,dist+1,i,j-1)

    # Right
    if (boundary(i,j+1) and visit(chess,i,j+1)):
        shortestPath(chess,dist+1,i,j+1)

    #if nothing of this happens then remove visited to 0,0
    visited[i][j]=0

if __name__ == '__main__':

    #testing the code
    chess = np.random.randint(2,size=(8,8))

    shortestPath(chess,0,0,0)

    if(minDist != 65535):
        print(minDist)
    else:
        print(-1)






