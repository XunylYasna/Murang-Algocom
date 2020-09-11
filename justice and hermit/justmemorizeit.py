def solve(n,a,b):
    MAX = int(3e5)
    dp = [0] * MAX
    
    dp[0] = a
    dp[1] = b
    
    for i in range(MAX):
        if n >= 2:
            dp[i] = min(a + dp[i - 1], b + dp[i - 2])
    
    return dp[n]
    
q, a, b = list(map(int,input().rstrip().split(" ")))
outs = []
for i in range(q):
    n = int(input().rstrip())
    outs.append(solve(n,a,b))
print("{}".format("\n".join(list(map(str,outs)))))