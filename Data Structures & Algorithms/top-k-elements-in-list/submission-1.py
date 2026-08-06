class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_1 = {}
        for num in nums:
            k_1[num] = 1 + k_1.get(num, 0)
        print(k_1)
        
        heap = []
        for num in k_1.keys():
            heapq.heappush(heap, (k_1[num],num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res