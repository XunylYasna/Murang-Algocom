# Check if possible given speed
def simulate(gates,vs, hs):
    check = True
    for i in range(len(gates)):
        return
    return check


# Get Input
w,v,n = list(map(int, input().strip().split()))

gates = []

for i in range(n):
    x,y = list(map(int, input().strip().split()))
    gates.append([x,y,x+w,y])

ss = (int,input())
s = []
for i in range(ss):
    s.append(int,input())
s.sort()
# Check if slowest speed can do it
if(not simulate(gates,s[0],v)):
    print('IMPOSSIBLE')
else:   
    # Binary search speed
    lo = 0
    hi = len(s)

    while lo < hi:
        middle = lo + (hi - lo)//2

        if simulate(gates,s[middle],v):
            lo = middle + 1
        else:
            hi = middle
    print(s[lo])