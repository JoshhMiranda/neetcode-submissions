class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold_list = []

        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    sold_list.append(prices[j] - prices[i])

        if len(sold_list) == 0:
            return 0
        else:
            return max(sold_list)
                    



        