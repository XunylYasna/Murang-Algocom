class PriorityQueue(object): 
    def __init__(self): 
        self.queue = []
        self.splits = [] 

    def __str__(self): 
        return ' '.join([str(i) for i in self.queue])

    def length(self):
        return len(self.queue)

    def initSplit(self, split):
        self.splits = split
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data)

    def split(self):
        mindex = self.getMaxIndex()
        value = self.queue[mindex][0]
        town = self.queue[mindex][1]
        for i in range(self.length()):
            if self.queue[i][1] == town: 
                del self.queue[i]
        
        self.queue.append([value // self.splits[town] + value % self.splits[town], town])
        for i in range(self.splits[town]):
            self.queue.append([value // self.splits[town], town])

        self.splits[town] += 1
        

        return

    # for getting Max Index
    def getMaxIndex(self): 
        max = 0
        for i in range(self.length()): 
            if self.queue[i][0] > self.queue[max][0]: 
                max = i 
        return max 

    # for getting Max Value
    def getMaxValue(self): 
        return self.queue[self.getMaxIndex()][0]
  
def solution(towns, hiding, townPeeps):
    splits = [1] * towns.length()
    towns.initSplit(splits)

    while(towns.length() < hiding):
        towns.split()
        print(towns)

    return towns.getMaxValue()

if __name__ == '__main__': 
    towns = PriorityQueue()
    allcitizen = 0
    maxP = 0
    townPeeps = []
    p, n = list(map(int, input().strip().split())) #hiding places, towns
    for i in range(n):
        peeps = int(input().rstrip())
        towns.insert([peeps, i]) # number of people in town, i is id of town
        townPeeps.append(peeps)
        

    print(solution(towns, p, townPeeps))
   