MOD = int(1e9) + 7

def recursion(sr,sc,dr,dc,ml):
    if sr == dr and sc == dc:
        return 1
    
    if ml == 0 or sr > 7 or sr < 0 or sc > 7 or sc < 0:
        return 0

    else:
        # left recursion(sr-1,sc,dr,dc,ml-1)
        # right recursion(sr+1,sc,dr,dc,ml-1)
        # up recursion(sr,sc+1,dr,dc,ml-1)
        # down recursion(sr,sc-1,dr,dc,ml-1)
        # up left recursion(sr-1,sc+1,dr,dc,ml-1)
        # up right recursion(sr+1,sc+1,dr,dc,ml-1)
        # down left recursion(sr-1,sc-1,dr,dc,ml-1)
        # down right recursion(sr+1,sc-1,dr,dc,ml-1)
        return recursion(sr-1,sc,dr,dc,ml-1) + recursion(sr+1,sc,dr,dc,ml-1) + recursion(sr,sc+1,dr,dc,ml-1) + recursion(sr,sc-1,dr,dc,ml-1) + recursion(sr-1,sc+1,dr,dc,ml-1) + recursion(sr+1,sc+1,dr,dc,ml-1) + recursion(sr-1,sc-1,dr,dc,ml-1) + recursion(sr+1,sc-1,dr,dc,ml-1)

def solve(source_row,source_col,dest_row,dest_col,moves_left):
    
    board = [[[0 for m in range(moves_left+1)] for y in range(8)] for x in range(8)] # 3d array (x,y) coordinates + moves
    # print(board)
    # print('BT',board[1][0][0])
    # print("dest",dest_row,dest_col)
    board[dest_row][dest_col][0] = 1 # start with destination with 0 moves left
    #populate 3d array
    for m in range(moves_left):
        for x in range(8):
            for y in range(8):
                right = x+1
                left = x-1
                up = y+1
                down = y-1
                if(right <= 7): #if king can go right
                    board[x][y][m+1] += board[right][y][m] #right
                    if(up <= 7):
                        board[x][y][m+1] += board[right][up][m] #upper right
                    if (down >= 0):
                        board[x][y][m+1] += board[right][down][m] # lower right

                if(left >= 0):
                    board[x][y][m+1] += board[left][y][m] #left
                    if(up <= 7):
                        board[x][y][m+1] += board[left][up][m] #upper left
                    if (down >= 0):
                        board[x][y][m+1] += board[left][down][m] #lower left
                
                if(up <= 7):
                    board[x][y][m+1] += board[x][up][m] #up
                if (down >= 0):
                    board[x][y][m+1] += board[x][down][m] #down

    
    return board[source_row][source_col][moves_left] % MOD
    # count = recursion(source_row,source_col,dest_row,dest_col,moves_left)
    # return count % MOD
	# compute and return answer here
    

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
# print(sr,sc)
print("{}".format(solve(sr,sc,dr,dc,k)))