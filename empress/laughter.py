def solve(i,k):
  # solve problem here. Return correct answer
    first = 'H'
    second = 'A'

    if(i == 0):
        return first

    if(i == 1):
        return second

    for n in range(i-2):
        first = first + second
        second = second + first

    if(i % 2 == 0):
        # return first[k]
        return first
    else:
        # return second[k]
        return second

    # return first[k]


i, k = list(map(int,input().rstrip().split(" ")))
print(solve(i,k))