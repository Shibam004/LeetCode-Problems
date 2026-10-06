1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        end = len(s) - 1
4
5        while s[end] ==  :
6            end = end - 1
7
8        start = end
9
10        while start >= 0 and s[start] !=  :
11            start = start - 1
12
13        return end - start
14        