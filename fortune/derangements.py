MOD = 1000000007
MAX_I = 300000

dp = [0] * (MAX_I + 1)
for i in range(0,MAX_I + 1):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 0
    else:
        dp[i] = ((dp[i - 1] + dp[i - 2]) * (i - 1)) % MOD
        
q = int(input().rstrip())
outs = []
for i in range(q):
    n = int(input().rstrip())
    outs.append(dp[n])
print("{}".format("\n".join(list(map(str,outs)))))