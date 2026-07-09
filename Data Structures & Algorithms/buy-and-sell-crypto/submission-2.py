class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        lowest_buy = prices[0]
        max_prof = 0

        buy_ptr = 0
        sell_ptr = 1
        while sell_ptr < len(prices):
            print("psp", prices[sell_ptr])
            if prices[sell_ptr] < lowest_buy:
                lowest_buy = prices[sell_ptr]
                print("lb", lowest_buy)
            profit = prices[sell_ptr] - lowest_buy
            print("profit", profit)
            if profit > max_prof:
                max_prof = profit
                print("max_prof", max_prof)
            sell_ptr += 1
        return max_prof
            