class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        profit = 0

        while p2 < len(prices):
            buy = prices[p1]
            sell = prices[p2]

            if buy > sell:
                p1 = p2
            elif buy < sell:
                profit = max(profit, sell-buy)
            p2 +=1
        return profit



        