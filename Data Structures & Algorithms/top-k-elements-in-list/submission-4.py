from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count_map = defaultdict(list)
        output = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            count_map[c].append(n)

        for i in range(len(nums), 0, -1):
            if k > 0 and count_map[i]:
                nums = count_map[i]
                for num in nums:
                    output.append(num)
                    k -= 1
            if k == 0:
                break

        return output        
        
