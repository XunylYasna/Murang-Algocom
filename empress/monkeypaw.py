# Get Final
def getLastMovie(arr,a,k): #a budget k price per ticket
    
    if(a < k):
        print(-1)
        return

    arr.sort()
    i = a // k
    if(i > len(arr)):
        i = len(arr)
        print(arr[0])
        return
    
    else:
        ans = arr[len(arr) - i]
        print(str(ans))
    return
        

n = int(input()) #number of movies
movies = []
for i in range(n):
    r,c = list(map(int,input().rstrip().split(" "))) #runtime, credits
    movies.append(r-c)

q = int(input()) # number of queries
for cc in range(q):
    s,e,a,k = list(map(int,input().rstrip().split(" "))) #s start index, e end index, a budget, k price per ticket, 
    # solve for answer here
    getLastMovie(movies[s:e+1],a,k)