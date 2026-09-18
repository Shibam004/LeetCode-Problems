1from typing import List
2from collections import deque
3
4class Solution:
5    def minMoves(self, classroom: List[str], energy: int) -> int:
6        m = len(classroom)
7        n = len(classroom[0])
8
9        id = [[-1] * n for _ in range(m)]
10
11        k = 0
12        sr = 0
13        sc = 0
14
15        for r in range(m):
16            for c in range(n):
17                if classroom[r][c] == 'S':
18                    sr = r
19                    sc = c
20                elif classroom[r][c] == 'L':
21                    id[r][c] = k
22                    k += 1
23
24        if k == 0:
25            return 0
26
27        total_mask = (1 << k) - 1
28
29        best = [
30            [
31                [-1] * (1 << k)
32                for _ in range(n)
33            ]
34            for _ in range(m)
35        ]
36
37        queue = deque()
38
39        best[sr][sc][0] = energy
40        queue.append((sr, sc, 0, energy, 0))
41
42        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
43
44        while queue:
45            r, c, mask, e, moves = queue.popleft()
46
47            for dr, dc in directions:
48                nr = r + dr
49                nc = c + dc
50
51                if nr < 0 or nr >= m or nc < 0 or nc >= n:
52                    continue
53
54                if classroom[nr][nc] == 'X':
55                    continue
56
57                ne = e - 1
58
59                if ne < 0:
60                    continue
61
62                nmask = mask
63
64                if classroom[nr][nc] == 'R':
65                    ne = energy
66
67                if classroom[nr][nc] == 'L':
68                    nmask |= 1 << id[nr][nc]
69
70                if nmask == total_mask:
71                    return moves + 1
72
73                if ne <= best[nr][nc][nmask]:
74                    continue
75
76                best[nr][nc][nmask] = ne
77
78                queue.append((nr, nc, nmask, ne, moves + 1))
79
80        return -1