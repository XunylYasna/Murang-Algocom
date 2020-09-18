def solve(s1,s2,n,m):
    
    dp = [[0 for x in range(m + 1)] for x in range(n + 1)] 
    
    for i in range(n+1):
        for j in range(m+1):
            
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1])
    
    return dp[n][m]
    
    
s1 = input().rstrip()
s2 = input().rstrip()
n = len(s1)
m = len(s2)
print("{}".format(solve(s1,s2,n,m)))