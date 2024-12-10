class Solution(object):
    def maxSubArray(self, nums):
        curr=0
        maxi=nums[0]
        start=end=0
        
        for i in range(len(nums)):
            if len(nums)<=1:
                return nums[i]
            curr+=nums[i]
            if curr>maxi:
                maxi=curr
                end=i
            if curr<0:
                curr=0
                start=i+1    
        return maxi    
