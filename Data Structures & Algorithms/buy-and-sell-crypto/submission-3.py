class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == [] or len(prices) == 1:
            return 0
        max_profit = 0
        buy_price = prices[0]
        buy_day = -1

        head = 0
        tail = 1
        while tail < len(prices):
            #print(buy_day, max_profit, head, tail)
            prof = prices[tail] - prices[head]
            if prof > max_profit:
                max_profit = prof
            if prices[tail] < buy_price:
                buy_price = prices[tail]
                buy_day = tail
                head = buy_day
                tail += 1
            else:
                tail += 1
        return max_profit
