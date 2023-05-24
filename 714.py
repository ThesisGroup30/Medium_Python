class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cash = 0
        hold = -prices[0]

        for i in range(1, n):
            prev_cash = cash
            prev_hold = hold
            cash = max(prev_cash, prev_hold + prices[i] - fee)
            hold = max(prev_hold, prev_cash - prices[i])

        return cash
