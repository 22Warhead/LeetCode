class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        j = len(nums)-1
        i = 0
        flagi = True
        flagj = True
        while i <= j:
            if nums[i] == target:
                ans[0] = i
                flagi = False
            if nums[j] == target:
                ans[1] = j
                flagj = False
            i += 1 if flagi else 0
            j -= 1 if flagj else 0
            if not flagi and not flagj:
                return ans
        return [-1, -1]
