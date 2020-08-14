def solve(L, n, coverage):
    counter = 0 #number of people who can cover the facade
    coverage.sort()

    for i in range(n):
        

    return counter

L, n = list(map(int,input().rstrip().split(" ")))
coverage = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
print(solve(L,n,coverage))