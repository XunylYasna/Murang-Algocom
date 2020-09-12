q, a, b = list(map(int,input().rstrip().split(" ")))
MAX = int(3e5) + 1
dp = [0] * MAX 

dp[0] = a
dp[1] = b

for i in range(2, MAX):
    dp[i] = min(a + dp[i - 1], b + dp[i - 2])
    
outs = []
for i in range(q):
    n = int(input().rstrip())
    outs.append(dp[n])
print("{}".format("\n".join(list(map(str,outs)))))