import re
import heapq
from heapq import heapify, heappop, heappush
import sys

def sum_all(n,num_list):
    counter = 0
    
    heapq.heapify(num_list)
    while len(num_list) > 1:
        num_list = sorted(num_list)
        
        front_num = heappop(num_list)
        next_num = heappop(num_list)

        cur_sum = front_num + next_num
 #       print(cur_sum//2)
        counter = counter + cur_sum//2
        heappush(num_list, cur_sum)
#         min_cost += cur_sum

    return counter + sum(num_list)


# str = 'I think I like eating soup because soup is the best thing to like eating.'.lower()

lines = []
while True:
    try:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    except EOFError:
        break
        

text = ''.join(lines)
text = re.findall(r'\w+', text) #removes all punctuations and splits the string per word
print(text)
temp = set(text) #get unique words
frequency = []

for word in temp : 
        frequency.append(text.count(word)) #initalize array of frequencies
    
print(frequency)
# num_list = [2,1,2,2,2,1,1,1,1,1,1]
print(sum_all(len(frequency), frequency))