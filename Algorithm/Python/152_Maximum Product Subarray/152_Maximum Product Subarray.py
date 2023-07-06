nums = [2, -5, -2, -4, 3]
max_num = nums[0]
min_num = nums[0]
for i in range(1, len(nums)-1):
    max_num = max(max_num * nums[i], nums[i])
    min_num = min(min_num * nums[i], nums[i])

print(max_num)
