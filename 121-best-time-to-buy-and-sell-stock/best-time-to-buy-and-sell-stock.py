class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price_seen = prices[0]
        max_profit_seen = 0
        for p in prices:
            if p < lowest_price_seen:
                lowest_price_seen = p
            else:
                profit_now = p - lowest_price_seen
                if profit_now > max_profit_seen:
                    max_profit_seen = profit_now
        return max_profit_seen