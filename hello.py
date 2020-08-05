import math

def bit_calculator(year):
    return 2**(int(year/10) - 194)


y = -1

while(y != 0):
    y = int(input())
    if(y == 0):
        break
    else:
        bit = bit_calculator(y)
        highest = math.log2(2**bit)
        biggestf = 1
        equation = math.log2(biggestf)
        while(equation <  highest):
            equation += math.log2(biggestf)
            biggestf += 1
        
        print(biggestf - 2)
