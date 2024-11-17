class Solution(object):
    def canJump(self, nums):
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])    
        return True   
