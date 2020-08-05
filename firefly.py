def getCollision(arr,key):
    # Get lower bound
    lo = 0
    hi = len(arr)

    while lo < hi:
        middle = lo + (hi - lo)//2

        if arr[middle] < key:
            lo = middle + 1
        else:
            hi = middle
    
    return len(arr) - lo

def calculate(bottom,top,h):
    # Set max
    m = len(bottom) * 2
    l = h
    bottom.sort()
    top.sort()
    
    # print(top)
    # print(bottom)
    for i in range(h):
        t = getCollision(top, h - i - 0.5)
        b = getCollision(bottom,i + 0.5)
        # print(t * -1,b)
        tc = t + b
        if(tc < m):
            m = tc
            l = 0
        if(tc == m):
            l += 1
            # print(str(tc) + " tc")
            # print(i * -1)

    print(str(m) + " " + str(l))
    return


n, h = list(map(int, input().strip().split()))
bottom = []
top = []
for i in range(n//2):
    bottom.append(int(input()))
    top.append(int(input()))

calculate(bottom,top,h)
