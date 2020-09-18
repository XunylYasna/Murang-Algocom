a,b,c,d,q = list(map(int,input().strip().split(" ")))
MOD = int(1e9)+7
MAX = 2 * int(1e4)
# perform any preprocessing needed here
f = [0] * (MAX + 1)
g = [0] * (MAX + 1)

for i in range(0, MAX + 1):
    f[0] = a
    g[0] = b
    f[1] = ( c * f[0] ) % MOD
    g[1] = ( c * g[0] ) % MOD
    
    if i >= 2 :
        f[i] = ( (c * f[i-1]) + (d * g[i-2]) ) % MOD
        g[i] = ( (c * g[i-1]) + (d * f[i-2]) ) % MOD

outs = []
for i in range(q):
    ni = int(input().strip())
    
    f_ans = str(f[ni])
    g_ans = str(g[ni])
    # compute and store proper values of f(n) and g(n) here in f_ans and g_ans respectively
    
    
    outs.append(" ".join([f_ans,g_ans]))
print("\n".join(outs))