MOD = int(1e9) + 7
MAX = 2 * int(1e5)
a, n, Q = list(map(int,input().strip().split(" ")))

der = [0] * MAX

# perform any preprocessing needed here
for i in range(0, MAX):
    if i < n:
        der[i] = a
    else:
        der[i] = (der[i-n] + der[i-n+1]) % MOD

outs = []
for i in range(Q):
    qi = int(input())
    # append the correct answer to the outs list here
    outs.append(der[qi])
print("\n".join(list(map(str,outs))))