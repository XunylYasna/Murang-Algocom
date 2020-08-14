n, f, k = list(map(int,input().rstrip().split(" ")))
vamps = [int(input()) for x in range(n)]
ans = ""
# solve answer here
vamps.sort()

for i in range(k):
    f -= vamps[i]
    if(f >= 0):
        ans = "YES"
    else:
        ans = "NO"

print(ans)