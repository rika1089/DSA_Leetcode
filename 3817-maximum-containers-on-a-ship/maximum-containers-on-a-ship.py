class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        containers = n * n
        noofcontainers = 0
        for i in range(1,containers+1) :
            if w * i <= maxWeight :
                noofcontainers += 1
        
        return noofcontainers
                
