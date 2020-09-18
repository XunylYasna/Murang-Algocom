MOD = int(1e9) + 7

memoization = [[[False for k in range(21)] for j in range(501)] for i in range(501)]
portalBoard = [[False for i in range(501)] for j in range(501)]
row = 0
col = 0


def recursion(r, c, k):
    # bounds
    if c > col:
        return 0

    if c < 1:
        return 0

    # base case
    if r == row:
        return 1

    # memoization
    if memoization[r][c][k]:
        return memoization[r][c][k]

    # else
    else:
        # if the current position is a portal and the checker can travel
        if portalBoard[r][c] and k > 0:
            destination = portalBoard[r][c]
            memoization[r][c][k] = (
                recursion(destination[0], destination[1], k - 1)
                + recursion(r + 1, c + 1, k)
                + recursion(r + 1, c - 1, k)
            ) % MOD
            return memoization[r][c][k]
        # if the current position is not a portal
        else:
            memoization[r][c][k] = (
                recursion(r + 1, c + 1, k) + recursion(r + 1, c - 1, k)
            ) % MOD
            return memoization[r][c][k]


r, c, p, k = list(map(int, input().strip().split(" ")))
row = r
col = c
rstart, cstart = list(map(int, input().strip().split(" ")))
for i in range(p):
    srR, srC, dsR, dsC = list(map(int, input().strip().split(" ")))
    portalBoard[srR][srC] = [dsR, dsC]
    portalBoard[dsR][dsC] = [srR, srC]


print(recursion(rstart, cstart, k))
