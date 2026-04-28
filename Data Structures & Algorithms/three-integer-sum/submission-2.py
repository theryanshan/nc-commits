class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    l += 1
        return result