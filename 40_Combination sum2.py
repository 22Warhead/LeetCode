class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backer(n, target, path):
            if target == 0:
                if path[:] not in ans:
                    ans.append(path[:])
                return
            if target < 0:
                return
            for i in range(n, len(candidates)):
                if i > n and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backer(i + 1, target - candidates[i], path)
                path.pop()

        backer(0, target, [])
        return ans
