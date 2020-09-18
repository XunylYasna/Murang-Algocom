import math

MOD = 1000000007

q = int(input().rstrip())
ans_list = []
for i in range(q):
	n, r = list(map(int,input().rstrip().split(" ")))
    ans = 0
    
print("\n".join(list(map(str,ans_list))))