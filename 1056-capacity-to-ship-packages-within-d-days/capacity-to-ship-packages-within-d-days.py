class Solution:
    def possible_hrs(self, weights: List[int], days: int, capacity : int) -> int:
        load = 0
        days = 0
        for i in range(len(weights)) :
            if load + weights[i] > capacity :
                days += 1
                load = weights[i]
            else :
                load += weights[i]
        return days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # if len(weights) == days :
        #     return max(weights)
        low,high = max(weights),sum(weights)

        while low <= high :
            mid = low + ( high - low ) // 2

            if self.possible_hrs(weights,days,mid) < days :
                high = mid - 1
            else :
                low = mid + 1
        return low




        