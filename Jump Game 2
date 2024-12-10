class Solution(object):
    def jump(self, nums):
        current=0
        dist=0
        jump=0
        for i in range(len(nums)-1):
            dist=max(dist,i+nums[i])
            if i==current:
                jump+=1
                current=dist
        return jump 
