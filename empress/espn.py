def md(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def upperbound(arr,key):
    # Get lower bound
    lo = 0
    hi = len(arr)

    while lo < hi:
        middle = lo + (hi - lo)//2

        if arr[middle] <= key:
            lo = middle + 1
        else:
            hi = middle
    return lo

# Driver

n, kx, ky = list(map(int,input().rstrip().split(" "))) #kx ky karen position
# people = [list(map(int,input().rstrip().split(" "))) for i in range(n)] #position of people
distance = []
for i in range (n):
    x1,y1 = list(map(int,input().rstrip().split(" ")))
    distance.append(md(x1,y1,kx,ky))

distance.sort()

q = int(input().rstrip()) # queries
for cc in range(q):
    e = int(input()) # energy
    ans = upperbound(distance,e)
    print(ans)