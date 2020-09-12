n, k = list(map(int,input().rstrip().split(" ")))
dp = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
MOD = 1000000007

if n > 1:
    for i in range(n-2, -1, -1):
        dp[i][0] += min(dp[i+1][0], dp[i+1][1] + k)
        dp[i][1] += min(dp[i+1][1], dp[i+1][0] + k)


print(min(dp[0][0], dp[0][1]))