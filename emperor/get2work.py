def count_cars(emp):
    emp.sort(key=lambda x: x[1])
    count = 0
    empleft = len(emp)
    # print(emp,"-count emp")
    if(empleft <= 0):
        return count
    for e in reversed(emp):
        empleft = empleft - e[1]
        count += 1
        if(empleft <= 0):
            return count

    return -1


def solution(tc, nt, loc, emp):
    answer = []
    # print(loc)
    for i in range(nt): # loop through towns
        if(i + 1 == loc):
            answer.append(0) # automatically append 0 cars if the town is in the same location
        else:
            filtered_emp = [employee for employee in emp if employee[0] == i + 1] # get employees from the town
            cars = count_cars(filtered_emp)

            if(cars == -1):
                return  "Case #" + str(tc) + ": IMPOSSIBLE"

            answer.append(cars)

    ans = "Case #" + str(tc) + ":"

    for x in answer:
        ans = ans + " " + str(x)

    return ans


c = int(input()) # cases
for i in range(c):
    emp = []
    n,t = list(map(int,input().rstrip().split(" "))) #num towns, office location
    e = int(input()) # num employees
    for m in range(e):
        h,p = list(map(int,input().rstrip().split(" "))) #home town, passenger
        emp.append([h,p])
    print(solution(i+1, n, t, emp))