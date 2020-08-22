import re
import heapq
from heapq import heapify, heappop, heappush


def sum_all(n,num_list):
    counter = 0
    

    heapq.heapify(num_list) #sort 

    while len(num_list) > 1:
        
        front_num = heappop(num_list)
        next_num = heappop(num_list)

        cur_sum = front_num + next_num
        counter = counter + min(front_num,next_num)
        heappush(num_list, cur_sum)

    return counter + sum(num_list)


# str = 'I think I like eating soup because soup is the best thing to like eating.'.lower()
str = []
while True:
    try:
        line = input()
        if line:
            str.append(line)
        else:
            break
    except EOFError:
        break
        

str = ''.join(str)
str = str.lower()
    

str = re.findall(r'\w+', str)

str2 = set(str)
num_list = []

for word in str2 : 
        # print('Frequency of ', word , 'is :', str.count(word))
        num_list.append(str.count(word))
    
# print(num_list)
# num_list = [2,1,2,2,2,1,1,1,1,1,1]
print(sum_all(len(num_list), num_list))