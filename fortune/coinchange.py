d, q = list(map(int,input().rstrip().split(" ")))
denoms = sorted(list(map(int,input().rstrip().split(" "))))

MAX = int(3e5) + 1

dp = [0] * MAX
dp[0] = 1

for denom in denoms:
    for i in range(1, MAX):
        if denom <= i:
            dp[i] += dp[i-denom]

ans_list = []
for i in range(q):
    v = int(input().rstrip())
    
    # build answer to avoid TLE
    # you can redefine the solve function as needed
    ans_list.append(dp[v])
print("{}".format("\n".join(list(map(str,ans_list)))))