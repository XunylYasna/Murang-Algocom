def getOne(string):
    first = "pqrst"
    second ="N"
    third = "KACE"

    
    if(len(string) < 1):
        return ""

    char = string[0]

    if char in first:
        return char
    
    if char in second:
        temp = getOne(string[1:])
        if temp == "":
            return ""
        return string[0] + temp

    if char in third:
        temp1 = getOne(string[1:])
        if(temp1 == ""):
            return ""
        temp2 = getOne(string[len(temp1)+1:])
        if(temp2 != ""):
            return string[0] + temp1 + temp2
    
    return ""

def solution(string):
    curr = ""
    first = "pqrst"
    second ="N"
    third = "KACE"
    end = 0
    i = 0
    
    while i < len(string):
        temp = ""
        char = string[i]

        if char in first:
            temp = char
        
        elif char in second:
            temp = getOne(string[i:]) #get substring and end index of the N operator
            if temp != "": #invalid N operator
                i = i + len(temp) - 1

        elif char in third:
            #get substring and end index of the KACE operators (two wffs)
            temp1 = getOne(string[i:])
            temp = temp1
            if temp != "":
                i = i + len(temp) - 1

        if len(temp) >= len(curr):
            curr = temp

        i+=1

    if curr == "":
        return "no WFF possible"
    return curr

n = input()
while(n != "0"):
    print(solution(n))
    n = input()