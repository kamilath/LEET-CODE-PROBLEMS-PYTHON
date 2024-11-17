class Solution(object):
    def jump(self, nums):
        end=0
        maxi=0
        jump=0
        for i in range(len(nums)-1):
            maxi=max(maxi,i+nums[i])
            if i==end:
                jump+=1
                end=maxi
        return jump   
