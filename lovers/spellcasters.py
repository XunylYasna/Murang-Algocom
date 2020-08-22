import math

def headache(a,n):
    return a * math.sin(n) + a * n

def solve(a,T):

    if(a == 0):
        return "Pat is the Best Tunnel Master!"
    
    lo = 0
    hi = 10**9
    while lo < hi:
        middle = lo + (hi - lo)//2
        h = headache(a,middle)
        
        if h == T:
            return int(middle)
        elif h < T:
            lo = middle + 1
        else:
            hi = middle

    
    return int(lo-1)

a, Q = list(map(int,input().strip().split(" "))) # a is constant
T = []
for i in range(Q):
    T = int(input()) # T is tresholds
    print("{}".format(solve(a,T)))