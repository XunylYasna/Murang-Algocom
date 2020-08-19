#Ansay, Henson, Landrito
def solve(L, n, coverage):
    coverage = sorted(coverage, key=lambda x: (x[0], -x[1]))
    facade_coverer = [coverage[0]]

    if(coverage[0][0] == 1 and coverage[0][1] == L):
        return n - 1
    if(coverage[0][0] != 1): #if there's no person who can cover first lot
        return "'Salem's Lot is doomed."
    else:
        j = 0
        for i in range(n): #gets all array that has farther reach and within interval
            if(facade_coverer[j][1] < coverage[i][1]): #checking the next array that has farther reach
                if(coverage[i][0] >= facade_coverer[j][0] and coverage[i][0] <= (facade_coverer[j][1])+1): #check if left bound if within the interval
                    facade_coverer.append(coverage[i])
                    j += 1
                else:
                    return "'Salem's Lot is doomed."
        
        if(facade_coverer[len(facade_coverer)-1][1] != L):
            return "'Salem's Lot is doomed."
        
        for i in range(1, len(facade_coverer)):
            if(i+1 == len(facade_coverer)):
                break
            if(facade_coverer[i+1][0] >= facade_coverer[i-1][0] and facade_coverer[i+1][0] <= facade_coverer[i-1][1]+1):
                facade_coverer.pop(i) #checks if the range of a person can be covered by another person
        
        return n - len(facade_coverer)
        
L, n = list(map(int,input().rstrip().split(" ")))
coverage = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
print(solve(L,n,coverage))
