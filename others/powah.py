def solve(e,t):
    if(t == 0):
        return 1

    lim = int(1e7)
    nt = t//2
    half = solve(e, nt) % lim
    temp = half * half % lim
    if(t % 2 == 1):
        temp = e * temp % lim
    return temp
  # solve for answer
  

e, t = list(map(int,input().rstrip().split(" ")))
print(solve(e,t))