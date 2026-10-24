class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #O(1)
        #I can use a linked list, biut jhow
        #does it even make sense as I can directly pass through using for loop
        # but that would be east. 
        l_1 = set()
        for i in nums:
            if i in l_1:
                return i
            else:
                l_1.add(i)
        return 0


        