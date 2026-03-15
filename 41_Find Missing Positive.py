class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            if nums[i] != x:
                return x
            if i != len(nums)-1 and nums[i] == nums[i+1]:
                continue
            x += 1
        return x
