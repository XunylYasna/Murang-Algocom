MOD = int(1e9) + 7
SIZE = 8


def solve(source_row,source_col,dest_row,dest_col,moves_left):
    grid = [[0 for row in range(8)] for col in range(8)]
    grid[source_row][source_col] = 1

    def inGrid(r,c):            
        return all(0<=coord<SIZE for coord in (r,c))

    def adjacentSum(pos, grid):
        r,c = pos
        total = 0
        for neighbor in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            delta_r,delta_c = neighbor
            (r2,c2) = (r+delta_r,c+delta_c)
            if inGrid(r2,c2):
                total += grid[r2][c2]
        return total        
	
    for _ in range(moves_left):
        grid = [[adjacentSum((r,c), grid) for r in range(8)] for c in range(8)]

    return grid[dest_row][dest_col] % MOD

    

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