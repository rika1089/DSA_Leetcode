class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1,ay1,ax2,ay2 = rec1
        bx1,by1,bx2,by2 = rec2

        return ax1 < bx2 and bx1 < ax2 and ay1 < by2 and by1 < ay2
        