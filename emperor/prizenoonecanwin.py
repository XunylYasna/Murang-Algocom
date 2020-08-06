def getMaxItems(arr, minprice):
    arr.sort()
    total = 1
    i=1
    while(i<len(arr)):
        if(arr[i] + arr[i-1] <= minprice):
            total=total+1
            
        i=i+1     
    return total
    
n, x = list(map(int,input().rstrip().split(" ")))
prices = list(map(int, input().rstrip().split(" ")))
print(getMaxItems(prices, x))