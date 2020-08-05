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

def calculate_waste(arr, x):
    return arr[lower_bound(arr,x)] - x

n, m = list(map(int, input().strip().split()))
sizes = []
wasted = 0


for i in range(n):
    sizes.append(int(input()))

sizes.sort()

for i in range(m):
    need = int(input())
    wasted += calculate_waste(sizes,need)

print(wasted)
