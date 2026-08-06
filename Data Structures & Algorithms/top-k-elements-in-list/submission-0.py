class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_1 = {}
        for i in nums:
            if i not in k_1.keys():
                k_1[i] = 1
            else:
                k_1[i] +=1
        sorted_items = sorted(k_1.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
        