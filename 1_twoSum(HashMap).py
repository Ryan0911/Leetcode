nums = [1, 2, 3, 4, 8, 9, 5, 7, 4, 5, 5]
target = 16
numMap = {}
for i in range(len(nums)):
    if numMap.__contains__(target-nums[i]):
        print([numMap.get(target-nums[i]), i])
    else:
        numMap[nums[i]] = i
