def solve(d,denoms,v):
    # compute and return answer here
    MAX = int(1e5)

    dp = [0] * (v+1)
    dp[0] = 1

    for denom in denoms:
        for i in range(1, len(dp)):
            if denom <= i:
                dp[i] += dp[i-denom]
    
    return dp[v]


d, q = list(map(int,input().rstrip().split(" ")))
denoms = sorted(list(map(int,input().rstrip().split(" "))))

# preprocess here

ans_list = []
for i in range(q):
    v = int(input().rstrip())
    
    # build answer to avoid TLE
    # you can redefine the solve function as needed
    ans_list.append(solve(d,denoms,v))
print("{}".format("\n".join(list(map(str,ans_list)))))