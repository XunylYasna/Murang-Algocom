def solve(n,nums):
  	# solve and return answer here
    count = 0
    total = 0
    has_pos = False
    
    for i in range(len(nums)):
        if nums[i] > 0:
            total += nums[i]
            count += 1
            has_pos = True
    
    if not has_pos:
        count = 1
        total = -9999
        for i in range(len(nums)):
            total = max(total, nums[i])
    
    return count, total

n = int(input())
nums = [int(input()) for i in range(n)]
ans, total = solve(n,nums)

print("{} {}".format(ans,total))