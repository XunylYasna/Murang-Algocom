import math

def bubbleSortAscending(arr):
    count = 0
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                count += 1

    return count

def bubbleSortDescending(arr):
    count = 0
    n = len(arr) 
    # print(arr,"fd")
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is less than 
            # than the next element 
            if arr[j] < arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                count += 1
                # print(arr)

    return count


def solve(books,n,s):
    # TODO: Compute and print answer here
    books1 = books.copy()

    sa = bubbleSortAscending(books)
    sd = bubbleSortDescending(books1)

    swaps = min(sa,sd)
    
    
    ans = s/swaps + 1
    # print(sa,sd,swaps, s, ans)
    #return quantum blasts per second (int)
    return math.floor(ans)
def main():
    n, s = list(map(int,input().strip().split(" "))) #num books, num blasts(hp)
    books = list(map(int,input().strip().split(" "))) #book ids
    print(solve(books,n,s))

if __name__ == "__main__":
    main()