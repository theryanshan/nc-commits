class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        unique = set(nums)
        
        for num in unique:
            if num - 1 not in unique:
                cur_len = 1
                while num + 1 in unique:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)
        return max_len