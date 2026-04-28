class Solution:
    def maxArea(self, heights: List[int]) -> int:
        global_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            left, right = heights[l], heights[r]
            local_area = (r - l) * min(left, right)
            global_max = max(global_max, local_area)

            if left <= right:
                l += 1
            else:
                r -= 1
        return global_max