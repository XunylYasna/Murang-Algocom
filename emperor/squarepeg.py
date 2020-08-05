# russ
import math
 
def plot_count(plot, house):
    count = 0
    # print(plot)
    # print(house)
    for p in plot:
        for h in house:
            if p > h:
                count += 1
                # print(p,h,"p h")
                house.remove(h)
                break
            else:
                break
        
 
    return count
 
n, m, k = list(map(int, input().rstrip().split(" ")))
radius = [int(i) for i in input().split()]
m_radius = [int(i) for i in input().split()]
k_sides = [int(i) for i in input().split()]

for i in k_sides:
    m_radius.append((math.sqrt(2 * (i**2)))/2) # hypotenuse of square given side

radius.sort()
m_radius.sort()
 
print(int(plot_count(radius, m_radius)))