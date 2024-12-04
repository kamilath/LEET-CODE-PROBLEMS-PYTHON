class Solution(object):
    def trap(self, height):
        if len(height)<=2:
            return 0
        ans=0
        left=0
        right=len(height)-1    
        lmax=height[0]
        rmax=height[-1]
        while left<=right:
            if lmax<height[left]:
                lmax=height[left]
            if rmax<height[right]:
                rmax=height[right]    
            if lmax<=rmax:
                ans+=lmax-height[left]    
                left+=1
            else:
                ans+=rmax-height[right]   
                right-=1
        return ans 
