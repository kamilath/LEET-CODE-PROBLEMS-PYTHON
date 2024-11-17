class Solution(object):
    def maxProfit(self, prices):
        mini=float('inf')
        maxi=0
        for i in prices:
            if i<mini:
                mini=i
            if i-mini>maxi:
                maxi=i-mini
        return maxi  
