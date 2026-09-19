1class Solution:
2    def checkOverlap(self, r: int, cx: int, cy: int, x1: int, y1: int, x2: int, y2: int) -> bool:
3        x = max(x1, min(cx, x2)) - cx
4        y = max(y1, min(cy, y2)) - cy
5
6        return x * x + y * y <= r * r