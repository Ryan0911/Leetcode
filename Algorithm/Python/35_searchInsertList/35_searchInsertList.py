nums = [1, 3, 5, 6]
target = 0


def binarySearch(left, right, arr, target):
    mid = (left + right)//2
    if(arr[mid] == target):
        return (mid)
    if(left > right):
        return left
    if(arr[mid] < target):  # turn right
        return binarySearch(mid+1, right, arr, target)
    if(arr[mid] > target):  # turn left
        return binarySearch(left, mid-1, arr, target)
    return 0


binarySearch(0, len(nums)-1, nums, target)
