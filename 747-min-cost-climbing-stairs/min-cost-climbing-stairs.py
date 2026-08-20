class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost_map = {}

        def mincost(curr,cost) :
            
            if curr in mincost_map :
                return mincost_map[curr]

            if curr == len(cost) :
                return 0

            if curr > len(cost) :
                return float('inf')
            
            oneStep = cost[curr] + mincost(curr+1,cost)
            twoStep = cost[curr] + mincost(curr+2,cost)

            mincost_map[curr] = min(oneStep,twoStep)

            return mincost_map[curr]

        return min(mincost(0,cost),mincost(1,cost))
