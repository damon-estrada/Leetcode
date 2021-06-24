class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # need to keep track of a current max and smallest value seen
        profit = 0
        days = len(prices)

        i = 0
        smallest_price = prices[i]

        while i < days:
            if prices[i] < smallest_price:
                smallest_price = prices[i]

            elif prices[i] - smallest_price > profit:
                profit = prices[i] - smallest_price
            i = i + 1

        return profit