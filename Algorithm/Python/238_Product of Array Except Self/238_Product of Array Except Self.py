nums = [1, 2, 3, 4]
left = [1, ]
right = [1, ]
right_i = 0
ans = []
for i in range(0, len(nums) - 1):
    left.append(left[i] * nums[i])
for i in range(len(nums) - 1, 0, -1):
    right.append(right[right_i] * nums[i])
    right_i = right_i + 1
for i in range(len(nums)):
    ans.append(left[i] * right[(len(nums)-1)-i])
print(ans)
