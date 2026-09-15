1class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        
4        def check(l, r):
5            while l < r:
6                if s[l] != s[r]:
7                    return False
8                l += 1
9                r -= 1
10            return True
11
12        n = len(s)
13        ans = 0
14        start = 0
15
16        for r in range(k - 1, n):
17            l = r - k + 1
18
19            if l >= start and check(l, r):
20                ans += 1
21                start = r + 1
22                continue
23            
24            l = r - k
25            if l >= start and check(l, r):
26                ans += 1
27                start = r + 1
28
29        return ans