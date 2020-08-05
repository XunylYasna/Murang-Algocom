def output(dh,kn):
    dh.sort()
    kn.sort()
    gold = 0

    for i in kn:
        # print("knight h" + str(i))
        while dh:
            head = dh.pop(0)
            if head <= i:
                gold += i
                break
                # print(str(i) + "killed"+str(head))
            else:
                dh.insert(0,head)
                break

    if len(dh) > 0 :
        return "Loowater is doomed!"
    else:
        return gold

n,m = list(map(int,input().rstrip().split(" ")))
while(n + m != 0):
    dh = []
    kn = []

    for i in range(n):
        dh.append(int(input()))

    for i in range(m):
        kn.append(int(input()))

    print(str(output(dh,kn)))
    n,m = list(map(int,input().rstrip().split(" ")))