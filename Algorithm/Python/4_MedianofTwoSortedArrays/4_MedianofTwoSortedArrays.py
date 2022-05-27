nums1 = [1, 2]
nums2 = [3, 4]


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1.sort()
        length = len(nums1) - 1
        if((length+1) == 1):
            return (float(nums1[0]))
        if((length+1) % 2 == 0):
            return ((float(nums1[int(length/2)]) + float(nums1[int((length/2)+1)]))/2)
        elif((length+1) % 2 != 0):
            return float(nums1[int((length/2))])


a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))
