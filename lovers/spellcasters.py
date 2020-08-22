import math

def solve(a,T):
    
    # if a == 0:
    #     return "Pat is the Best Tunnel Master!"

	# TODO: Compute and return answer here
    lo = 0
    hi = 10e+305
    while lo < hi:
        middle = lo + (hi - lo)//2
        h = a * math.sin(middle) + a * middle
        if h == T:
            return int(middle)
        elif h < T:
            lo = middle + 1
        else:
            hi = middle

    if(middle >= 10**10 - 1):
        return "Pat is the Best Tunnel Master!"
    return int(middle)

a, Q = list(map(int,input().strip().split(" "))) # a is constant
T = []
for i in range(Q):
    T = int(input()) # T is tresholds
    print("{}".format(solve(a,T)))