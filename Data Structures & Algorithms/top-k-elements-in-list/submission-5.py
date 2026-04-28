import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = {}
        heap = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while len(heap):
            output.append(heapq.heappop(heap)[1])

        return output