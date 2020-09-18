# Initialize priority queue. Put all N combos and their frequency. Order by frequency
# Build the K-ary huffman tree
# Output total number of button presses by traversing huffman tree



N, K = list(map(int, input().strip().split()))
F = []

for i in range(N):
    F.append(int(input()))