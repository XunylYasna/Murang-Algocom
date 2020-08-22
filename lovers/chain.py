def solve(cards):
    # cards.sort()
    room = 0
    i = 1
    while( i < 10):
        if(cards[i] > 0):
            room += 1
            cards[i] -= 1

        if(i == 9):
            if(cards[0] > 0):
                room += 1
                cards[0] -= 1
                i = 0
            else:
                i = 10
        i += 1

    return room

cards = list(map(int,input().strip().split(" ")))
print("{}".format(solve(cards)))