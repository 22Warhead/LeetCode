class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(n, target ,path):
            if target == 0:
                print(path)
                ans.append(path[:])
                return
            if target < 0:
                return
            for i in range(n, len(candidates)):
                path.append(candidates[i])
                backtracking(i, target-candidates[i],path)
                path.pop()

        backtracking(0, target, [])
        return ans
                
