class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_1 = len(set(nums))
        if len_1 != len(nums):
            return True
        else:
            return False
        