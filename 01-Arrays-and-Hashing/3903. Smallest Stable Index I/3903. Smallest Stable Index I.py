1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        for i in range(n):
5            instability = max(nums[0:i+1]) - min(nums[i:n])
6            if instability <= k:
7                return i
8
9        return -1
10
11        