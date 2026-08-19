class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = [(2,3,4,5),(4,5,6,7),(6,7,8,9)]
        reserved = {}

        # Group seats by row
        for r ,c in reservedSeats : 
            if r not in reserved :
                reserved[r] = set()
            reserved[r].add(c)
        total = 0

        # Check each row
        for row,seats in reserved.items() :
            
            left = all(s not in seats for s in (2,3,4,5))
            middle = all(s not in seats for s in (4,5,6,7))
            right = all(s not in seats for s in (6,7,8,9))

            if left and right :
                total += 2
            elif left or middle or right :
                total +=1
            # else no family can sit in that row
        total += 2 * (n - len(reserved))
        return total

            

