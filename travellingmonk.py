def lower_bound(arr, x):
    lo = 0
    hi = len(arr)

    while lo < hi:
        middle = lo + (hi - lo)//2

        if arr[middle] < x:
            lo = middle + 1
        else:
            hi = middle
    
    return lo


def get_height(t, he, ti):
    i = lower_bound(ti,t) - 1
    p1 = [he[i],ti[i]]
    p2 = [he[i+1], ti[i+1]]

    return float((t-p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0])

def find_intersect(h1,t1,h2,t2):
    lo = 0
    hi = min(float(t1[-1]), float(t2[-1]))
    tol = 0.0000001
    middle = 0
    while abs(lo - hi) > tol:
        middle = lo + (hi - lo)/2.0 #middle time

        a = get_height(middle,h1,t1)
        d = get_height(middle,h2,t2)

        if(a < d):
            lo = middle
        else:
            hi = middle

    return middle


a, d  = list(map(int, input().strip().split()))

h1 = [0]
t1 = [0]
h2 = []
t2 = [0]
peak = 0

for i in range(a):
    height,time = list(map(int, input().strip().split()))
    peak += height
    h1.append(h1[-1] + height)
    t1.append(t1[-1] + time)

h2.append(peak)
for i in range(d):
    height,time = list(map(int, input().strip().split()))
    h2.append(h2[-1]-height)
    t2.append(t2[-1] + time)

print("{:.6f}".format(round(find_intersect(h1,t1,h2,t2),6)))

