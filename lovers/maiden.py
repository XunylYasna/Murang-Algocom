def solve(n,c,vals):
    count = 1
 
    vals.sort(key = lambda x: x[1]) 
    
      
    endtemp = vals[0][1] 
      
    for i in range(1, len(vals)): 
        start = vals[i][0] 
        end = vals[i][1] 
          
        if start >= endtemp: 
            endtemp = end 
            count += 1

    return count * c

n, c = list(map(int,input().strip().split(" "))) #time periods, gold pieces
vals = [list(map(int,input().strip().split(" "))) for i in range(n)]
print("{}".format(solve(n,c,vals)))