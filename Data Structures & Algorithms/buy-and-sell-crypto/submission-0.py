class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        length = len(prices)

        best = 0
        while right < length:
            price = prices[right]-prices[left]
            if price < 0:
                left = right
                right = left+1
            else:
                best = max(best, price)
                right+=1
        return best


        