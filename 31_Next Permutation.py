class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        executed = False
        i = len(nums) - 2
        j = i + 1
        x = j
        while (i >= 0) and(nums[i] >= nums[i+1]):
            i -= 1
        if i >= 0:
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            if j >= 0:
                nums[i], nums[j] = nums[j], nums[i]
                executed = True
        i += 1
        while i < x:
            nums[i], nums[x] = nums[x], nums[i]
            i += 1
            x -= 1
