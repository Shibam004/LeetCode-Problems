1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
5        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
6        cnt = [[0] * (2 * n) for _ in range(2 * n)]
7        best = 0
8        for ax, ay in A:
9            for bx, by in B:
10                dx = bx - ax + n
11                dy = by - ay + n
12                cnt[dx][dy] += 1
13                best = max(best, cnt[dx][dy])
14        return best