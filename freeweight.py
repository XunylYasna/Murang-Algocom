def isPaired(row,w):
    # Check if every weight is paired
    pair = False
    weight = 0
    for i in range(len(row)):
        # Check if less than weight, remove
        if(row[i] > w):
            if pair:
                if weight == row[i]:
                    pair = False
                else:
                    return False
            else:
                weight = row[i]
                pair = True
    return not pair

# def removeLighter(row,key):
#     result = list(filter(lambda x: x > key, row))
#     return (result)

def checkRacks(r1,r2,w):
    return isPaired(r1,w) and isPaired(r2,w)

def get_heaviest(r1,r2,w):
    # Binary search list of weights
    lo = 0
    hi = len(w)
    middle = 0
    check = False
    while(lo < hi or not check):
        middle = lo + (hi-lo)//2
        if(checkRacks(r1,r2,w[middle])):
            check = True
            hi = middle
            
        else:
            lo = middle + 1
            check = False
    
    return w[middle]

n = (int, input())
r1 = list(map(int,input().strip().split()))
r2 = list(map(int,input().strip().split()))
w = []
w.extend(r1)
w.extend(r2)
w = list(dict.fromkeys(w))
w.append(0)
w.sort()
# print(w)

print(str(get_heaviest(r1,r2,w)))
