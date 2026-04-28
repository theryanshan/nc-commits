from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # Step 1: frequency map
        return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
            