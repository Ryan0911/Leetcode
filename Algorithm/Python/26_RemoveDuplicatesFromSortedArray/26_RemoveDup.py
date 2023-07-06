nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
dup = {}
count = 0
for index, i in enumerate(nums):
    if i not in dup:
        dup[i] = 1
    else:
        count += 1
        del nums[index]
print(count)
