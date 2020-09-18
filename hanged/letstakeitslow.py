MOD = int(1e9) + 7
a, n, Q = list(map(int,input().strip().split(" ")))

MAX = int(2e5) + 1
dp = [0] * MAX

for i in range(MAX):
    if i < n:
        dp[i] = a
    else:
        dp[i] = dp[i-n] + dp[i-n+1] % MOD

outs = []
for i in range(Q):
    qi = int(input())
    outs.append(dp[qi])
    
print("\n".join(list(map(str,outs))))