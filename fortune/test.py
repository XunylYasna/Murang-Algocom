

def solve(n,m,k,times):
	# compute and return answer here
    # n = y, m = x
    ystart = n - 2
    while ystart >= 0:
        for x in range(m):
    #         # get least possible value 
    #         # print(x,ystart,times[ystart][x],"--test")
            left = x - 1
            right = x + 1
            least = times[ystart+1][x]
            if left >= 0:
                val = times[ystart+1][left] + k
                least = min(least,val)
            if right < m:
                val = times[ystart+1][right] + k
                least = min(least,val)
            
            times[ystart][x] = times[ystart][x] + least
        # print(times)

        ystart = ystart - 1
    # print(times[ystart][1])

    return min(times[0])
    
n, m, k = list(map(int,input().rstrip().split(" ")))
times = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
print("{}".format(solve(n,m,k,times)))