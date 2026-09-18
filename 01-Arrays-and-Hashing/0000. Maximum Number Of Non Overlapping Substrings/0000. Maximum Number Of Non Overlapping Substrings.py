1class Solution:
2    def maxNumOfSubstrings(self, s: str) -> list[str]:
3        counts = Counter(s)
4        first = {c: s.find(c) for c in counts}
5        last = {c: s.rfind(c) for c in counts}
6
7        res = []
8        queue = deque()
9
10        for c in counts:
11            queue.appendleft([first[c], last[c], counts[c]])
12
13            left = inf
14            right = -inf
15            total = 0
16
17            for x, y, z in queue:
18                total += z
19                left = min(left, x)
20                right = max(right, y)
21
22                if total == right - left + 1:
23                    break
24
25            if total == right - left + 1:
26                res.append(s[left:right + 1])
27                queue.clear()
28
29        return res