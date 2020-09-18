def recursion(r, c, p, k, posR, posC, portals):
    if posR == r:  # if last row is reached
        return 1
    if k == -1:  # if too many portals are taken
        return 0

    # bound column
    if posC < 1:
        return 0
    if posC > c:
        return 0

    else:
        ans = 0
        # check current position if a portal can be accessed, travel through portal and recurse
        for portal in portals:
            if posR == portal[0] and posC == portal[1]:
                ans += recursion(r, c, p, k - 1, portal[2], portal[3], portals)
                if ans > 0:
                    ans -= 2

            if posR == portal[2] and posC == portal[3]:
                ans += recursion(r, c, p, k - 1, portal[0], portal[1], portals)

        return (
            ans  # portal travel
            + recursion(r, c, p, k, posR + 1, posC + 1, portals)  # diagonal right
            + recursion(r, c, p, k, posR + 1, posC - 1, portals)  # diagonal left
        )


MOD = int(1e9) + 7

r, c, p, k = list(
    map(int, input().strip().split(" "))
)  # numrows numcolumns numportals numPortalsCanTake
rstart, cstart = list(map(int, input().strip().split(" ")))
portals = [
    list(map(int, input().strip().split(" "))) for i in range(p)
]  # [srcR, srcC, desR, desC] can go both ways


# compute and print answer here
print(recursion(r, c, p, k, rstart, cstart, portals) % MOD)
