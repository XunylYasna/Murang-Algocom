def getDiscount(arr):
    arr.sort()
    dc = len(arr) // 3
    mod = len(arr) % 3
    disc = 0
    for i in range(dc):
        disc += arr[i * 3 + mod]
    
    return disc

n = int(input())
vals = list(map(int,input().rstrip().split(" ")))

print(getDiscount(vals))