class Solution(object):
    def maxProfit(self, prices):
        maxi=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                maxi+=prices[i+1]-prices[i]
        return maxi    
