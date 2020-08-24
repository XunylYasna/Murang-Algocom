#Ansay, Henson, Landrito

def solve(k,a,flist):
    MOD = 1000000007
    # k is n in F(n), a is array of A, 

    while k >= len(flist):
        newf = (a[len(flist)] + sum(flist)) % MOD
        flist.append(newf)
        # print(a[k],flist)
        
    return flist[k]

    
    
q, n = list(map(int,input().rstrip().split(" ")))
a = [int(input().rstrip()) for i in range(n)]
flist = [a[0]]
outs = []
for i in range(q):
    k = int(input().rstrip())
    outs.append(solve(k,a,flist))
print("{}".format("\n".join(list(map(str,outs)))))