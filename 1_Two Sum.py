class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        compare = {}
        for i in range(n):
            x = target - nums[i]
            if x in compare:
                return [compare[x], i]
            else:
                compare[nums[i]] = i

