def woodcut(arr):
    temp = []
    k = 0
    for i in arr:
        i.pop(0)
        temp.append(sum(i))  
    for i in temp:
        temp[k] = temp[k]*(len(temp)-k)
        k+=1
    return(sum(temp)/len(arr)*1.0000000000)
finalanswer = []
t = int(input())
for i in range(t):
    n = int(input())
    vals = []
    for i in range(n):
        vals.append(list(map(int,input().rstrip().split(" "))))
    print(woodcut(vals))