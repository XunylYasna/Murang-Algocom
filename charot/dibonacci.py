def solve(k,dibs):
    
    while k >= len(dibs):
        # print(dibs)
        newd = (dibs[len(dibs)-2] + dibs[len(dibs)-3]) % MOD
        dibs.append(newd)
        
    return dibs[k]
    

MOD = 1000000007
q = int(input().rstrip())
outs = []
dibs = [1,1,2,2,3,4,5,7]
for i in range(q):
	k = int(input().rstrip())
	outs.append(solve(k,dibs))
print("{}".format("\n".join(list(map(str,outs)))))