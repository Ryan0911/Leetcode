nums = [1, 2, 3, 4, 8, 9, 5, 7, 4, 5, 5]
target = 16
numMap = {}

for i in range(len(nums)):
    if nums[i] in numMap.keys():
        return [i, numMap[nums[i]]]
    else:
        numMap[target - nums[i]] = i
