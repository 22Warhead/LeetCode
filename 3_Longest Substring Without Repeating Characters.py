class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = s
        ans  = 0
        for i in range(len(x)-1):
            s = x[i]
            m = 1
            for j in range(i+1, len(x)):
                if x[j] in s:
                    break
                s += x[j]
                m += 1
            if m > ans:
                ans = m
            
        if ans == 0:
            return len(x)
        return ans
