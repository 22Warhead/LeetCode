class Solution:
    def expand(self, s, l ,r):
        while l >= 0 and r  < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return r-l-1
        
    def longestPalindrome(self, s: str) -> int:
        f, e = 0, 0
        for i in range(len(s)):
            x = self.expand(s, i, i)
            y = self.expand(s, i, i+1)
            z = max(x, y)
            if z > e-f:
                f = i-((z-1)//2)
                e = i + (z//2)
        return s[f:e+1]
