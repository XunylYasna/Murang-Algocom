def multiply(a, b): 
      
    # Creating an auxiliary matrix  
    # to store elements of the 
    # multiplication matrix 
    mul = [[0 for x in range(3)] 
              for y in range(3)]; 
    for i in range(3): 
        for j in range(3): 
            mul[i][j] = 0; 
            for k in range(3): 
                mul[i][j] += a[i][k] * b[k][j]
  
    # storing the multiplication 
    # result in a[][] 
    for i in range(3): 
        for j in range(3): 
            a[i][j] = mul[i][j] # Updating our matrix 
    return a

def power(a,b,c,F, n): 
    M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
  
    # Multiply it with initial values i.e  
    # with F(0) = 0, F(1) = 1, F(2) = 1 
    # if (n == 1): 
    #     return F[0][0] + F[0][1]; 
    if (n == 1): 
        return a
    
    if (n == 2): 
        return b
    
    if( n == 3):
        return c
    
    power(a,b,c,F, int(n / 2)); 
  
    F = multiply(F, F); 
  
    if (n % 2 != 0): 
        F = multiply(F, M)
  
    # Multiply it with initial values i.e  
    # with F(0) = 0, F(1) = 1, F(2) = 1 
    return F[0][0] + F[0][1]

def tribonacci(a,b,c,i):
    T = [[ 1, 1, 1 ],   
        [1, 0, 0 ], 
        [0, 1, 0 ]]

    # base condition 
    if (i == 1): 
        return a
    
    if (i == 2): 
        return b
    
    if( i == 3):
        return c

    else:
        power(T, i - 2)
    
    return T[0][0]

def solve(a,b,c,i):
    
    MOD = 1000000007
    i = i % MOD
	# compute and return answer here
    while(i > 3):
        i = i - 3
        a = a + b + c
        b = b + c + a
        c = c + a + b

    arr = [a,b,c]
    return arr[i-1]

    
a, b, c, i = list(map(int,input().rstrip().split(" ")))
# print(solve(a,b,c,i + 1))
print(tribonacci(a,b,c,i))