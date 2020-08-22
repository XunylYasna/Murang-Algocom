import math

def mergea(arr, temp, left, mid, right): 
    inv_count = 0
  
    i = left #i is index for left subarray*/ 
    j = mid #i is index for right subarray*/ 
    k = left #i is index for resultant merged subarray*/ 
    while ((i <= mid - 1) and (j <= right)): 
        if (arr[i] <= arr[j]): 
            temp[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp[k] = arr[j] 
            k += 1
            j += 1
  
            inv_count = inv_count + (mid - i) 

    while (i <= mid - 1): 
        temp[k] = arr[i] 
        k += 1
        i += 1

    while (j <= right): 
        temp[k] = arr[j] 
        k += 1
        j += 1
  
    for i in range(left,right+1,1): 
        arr[i] = temp[i] 
  
    return inv_count 

def merged(arr, temp, left, mid, right): 
    inv_count = 0
  
    i = left #i is index for left subarray*/ 
    j = mid #i is index for right subarray*/ 
    k = left #i is index for resultant merged subarray*/ 
    while ((i <= mid - 1) and (j <= right)): 
        if (arr[i] >= arr[j]): 
            temp[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp[k] = arr[j] 
            k += 1
            j += 1
  
            inv_count = inv_count + (mid - i) 

    while (i <= mid - 1): 
        temp[k] = arr[i] 
        k += 1
        i += 1

    while (j <= right): 
        temp[k] = arr[j] 
        k += 1
        j += 1
  
    for i in range(left,right+1,1): 
        arr[i] = temp[i] 
  
    return inv_count 
  

def _mergeSort(arr, temp, left, right, ad): 
    inv_count = 0
    
    if (right > left): 
        mid = int((right + left)/2) 

        inv_count = _mergeSort(arr, temp, left, mid, ad) 
        inv_count += _mergeSort(arr, temp, mid+1, right, ad) 

        if(ad == 1):
            inv_count += mergea(arr, temp, left, mid+1, right)
        else:
            inv_count += merged(arr, temp, left, mid+1, right)
  
    return inv_count 


def solve(books,n,s):
    # TODO: Compute and print answer here
    books1 = books.copy()
    temp = [0 for i in range(n)] 
    temp1 = [0 for i in range(n)] 

    sa = _mergeSort(books, temp, 0, n - 1,1) 
    sd = _mergeSort(books1, temp1, 0, n - 1,0) 
    # print(sa,sd, s)
    swaps = min(sa,sd)
    
    if swaps == 0:
        return "Butz loses!"
    
    ans = s/swaps + 1
    
    #return quantum blasts per second (int)
    return math.floor(ans)
def main():
    n, s = list(map(int,input().strip().split(" "))) #num books, num blasts(hp)
    books = list(map(int,input().strip().split(" "))) #book ids
    print(solve(books,n,s))

if __name__ == "__main__":
    main()