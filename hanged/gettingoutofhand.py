a,b,c,d,q = list(map(int,input().strip().split(" ")))
MOD = int(1e9) + 7
MAX = int(2e5) + 1
g = [0] * MAX
f = [0] * MAX

f[0] = a
g[0] = b 
f[1] = c * f[0] % MOD
g[1] = c * g[0] % MOD

for i in range(2, MAX):
    f[i] = (c * f[i-1] + d * g[i-2]) % MOD
    g[i] = (c * g[i-1] + d * f[i-2]) % MOD

outs = []
for i in range(q):
    ni = int(input().strip())
    
    f_ans = str(f[ni])
    g_ans = str(g[ni])

    outs.append(" ".join([f_ans,g_ans]))
print("\n".join(outs))