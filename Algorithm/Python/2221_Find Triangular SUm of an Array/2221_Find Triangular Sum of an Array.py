nums = [2, 6, 6, 5, 5, 3, 3, 8, 6, 4, 3, 3, 5, 1, 0, 1, 3, 6, 9]
if(len(nums) == 1):
    print(nums[0])
iteration = len(nums) - 1
while(iteration != 0):
    for i in range(0, iteration):
        nums[i] = (nums[i] + nums[i + 1]) % 10
    iteration = iteration - 1
print(nums[0])
