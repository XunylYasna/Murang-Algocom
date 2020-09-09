def solve(n,m,k,times):
    # compute and return answer here]
    MAX = int(1e4)

    dp = [0] * MAX
    

    
    
n, m, k = list(map(int,input().rstrip().split(" ")))
times = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
print("{}".format(solve(n,m,k,times)))