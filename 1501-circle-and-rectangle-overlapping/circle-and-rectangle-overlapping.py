class Solution:
    def point_lie_on_circle(self,radius: int, xCenter: int, yCenter: int, a: int, b:int) -> bool :
        # Check whether thr given point lies within the circle or not
        if ((xCenter - a)**2 + (yCenter - b)**2) <= radius**2  :     #  TC = O(1)
            return True
        return False

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        vertices = [(x1,y1),(x2,y2),(x1,y2),(x2,y1)] # All the vertices of the rectangle
        # 1. Check for all the vertices 
        for vertex in vertices :                                            # TC = O(1)
            a,b = vertex
            if self.point_lie_on_circle(radius,xCenter,yCenter,a,b) :
                return True
        
        # 2. Check if circle center is inside rectangle
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:                     # TC = O(1)
            return True

        # 3. Check closest point on rectangle edges
        closestX = min(max(xCenter, x1), x2)
        closestY = min(max(yCenter, y1), y2)
        if self.point_lie_on_circle(radius, xCenter, yCenter, closestX, closestY):   # TC = O(1)
            return True

        return False