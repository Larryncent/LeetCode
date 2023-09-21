class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l = buy, r = sell
        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP
