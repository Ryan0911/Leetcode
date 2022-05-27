nums = [1, 3, 2]
#nums = [2, 3, 1]
#nums = [1, 2, 3, 4, 5]
#nums = [1,1,1,1,1]
ans = 0
if(len(nums) == 1):
    print(0)
    # return 0
if(nums[0] >= len(nums)-1):
    print(1)
    # return 1
for i in range(0, len(nums)):
    nums[i] = i+nums[i]
current = 0
pre = 0
pos = 0
while current < len(nums)-1:
    ans += 1
    pre = current
    while pos <= pre:
        if(current < nums[pos]):
            current = nums[pos]
        pos += 1
print(ans)
