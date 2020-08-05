def match(w,u,b):
    # 
    longest = ""
    for char in u:
        w[0] = char + w[0]
    
    longest = w[0]

    i = 0
    # Match binary operators
    while len(b):
        if(len(w) < 2):
            break
        w[0] = b.pop() + w[0] + w.pop()

    return w[0]


def solution(string):
    first = "pqrst"
    second ="N"
    third = "KACE"

    wff = []
    unary = []
    binary = []

    for char in string:
        if char in first:
            wff.append(char)
    
    if wff == []:
        return "no WFF possible"

    for char in string:
        if char in second:
            unary.append(char)

    for char in string:
        if char in third:
            binary.append(char)

    return match(wff,unary,binary)
     


n = input()
while(n != "0"):
    print(solution(n))
    n = input()