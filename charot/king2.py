MOD = int(1e9) + 7
# import numpy as np

def solve(source_row,source_col,dest_row,dest_col,moves_left):
    firstboard = [ [0]*8 for i in range(8)]
    secondboard = [ [0]*8 for i in range(8)]
    emptyboard =  [ [0]*8 for i in range(8)]
    firstboard[dest_row][dest_col] = 1
    
    for m in range(moves_left):
        for x in range(8):
            for y in range(8):
                right = x+1
                left = x-1
                up = y+1
                down = y-1
                if(right <= 7): #if king can go right
                    secondboard[x][y] += firstboard[right][y]#right
                    if(up <= 7):
                        secondboard[x][y] += firstboard[right][up] #upper right
                    if (down >= 0):
                        secondboard[x][y] += firstboard[right][down] # lower right

                if(left >= 0):
                    secondboard[x][y] += firstboard[left][y]#left
                    if(up <= 7):
                        secondboard[x][y] += firstboard[left][up] #upper left
                    if (down >= 0):
                        secondboard[x][y] += firstboard[left][down] #lower left
                
                if(up <= 7):
                    secondboard[x][y] += firstboard[x][up] #up
                if (down >= 0):
                    secondboard[x][y] += firstboard[x][down] #down
        firstboard = secondboard.copy()
        secondboard = emptyboard.copy()
        # print(np.matrix(firstboard))
	
    return firstboard[source_row][source_col] % MOD

    

"""
This function converts the chess notation into 0-based row and columns

Parameters:

s - square in chess algebraic notation

Returns:

r - row value
c - column value
"""
def sq_to_loc(s):
    sr = ord(s[0]) - ord('A')
    sc = ord(s[1]) - ord('1')
    return sr,sc

k = int(input().rstrip())
src,dest = input().rstrip().split(" ")
sr,sc = sq_to_loc(src)
dr,dc = sq_to_loc(dest)
print("{}".format(solve(sr,sc,dr,dc,k)))