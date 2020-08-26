#Ansay, Henson, Landrito
def recurse(pos,n):
    if pos < 0:
        return 0
    if n == 0:
        if pos == 0:
            return 1
        else:
            return 0
    if pos//2 > n:
        return 0

    return recurse(pos - 1, n - 1) + recurse(pos + 1, n - 1)

def solve(n):
    MOD = 1000000007
    if n == 0:
        return 1
    
    if(n % 2 == 1):
        return 0
    
    else:
        pos = 0 
        return recurse(pos,n) % MOD
    # compute and return answer here
    

n = int(input().rstrip())
print(solve(n))