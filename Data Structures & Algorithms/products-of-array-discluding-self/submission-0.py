class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [0] * len(nums), [0] * len(nums)
        left[0], right[len(nums) - 1] = 1, 1
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        return [x * y for x, y in zip(left, right)]