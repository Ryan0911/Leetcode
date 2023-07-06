class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in nums:
            if i in hash_table.keys():
                return True
            else:
                hash_table[i] = 0
        return False
