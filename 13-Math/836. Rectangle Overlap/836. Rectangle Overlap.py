1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        cl = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
4        cw = min(rec2[3], rec1[3]) - max(rec1[1], rec2[1])
5
6        return cl > 0 and cw > 0
7        