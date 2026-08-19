class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # seats = [(2,3,4,5),(4,5,6,7),(6,7,8,9)]
        # reserved = {}

        # # Group seats by row
        # for r ,c in reservedSeats : 
        #     if r not in reserved :
        #         reserved[r] = set()
        #     reserved[r].add(c)
        # total = 0

        # # Check each row
        # for row,seats in reserved.items() :
            
        #     left = all(s not in seats for s in (2,3,4,5))
        #     middle = all(s not in seats for s in (4,5,6,7))
        #     right = all(s not in seats for s in (6,7,8,9))

        #     if left and right :
        #         total += 2
        #     elif left or middle or right :
        #         total +=1
        #     # else no family can sit in that row
        # total += 2 * (n - len(reserved))
        # return total

        # lets start with two families per row 
        seats = 2 * n
        reservedSeats.sort()
        i = 0

        while i < len(reservedSeats) :
            curr_row = reservedSeats[i][0]
            flag25,flag47,flag69 = 1, 1, 1

            while i < len(reservedSeats) and reservedSeats[i][0] == curr_row:
                seat = reservedSeats[i][1]
                if 2 <= seat <= 5:
                    flag25 = 0
                    if 4 <= seat <= 5:
                        flag47 = 0
                elif 6 <= seat <= 9:
                    flag69 = 0
                    if 6 <= seat <= 7:
                        flag47 = 0
                i += 1

            # Adjust answer based on blocked families
            if flag25 == 0 and flag47 == 0 and flag69 == 0:
                seats -= 2
            elif flag25 == 0 or flag47 == 0 or flag69 == 0:
                seats -= 1

        return seats 

            

