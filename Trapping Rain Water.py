class Solution(object):
    def trap(self, height):
        leftmax=0
        rightmax=0
        left=0
        right=len(height)-1
        t=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    t+=leftmax-height[left]   
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    t+=rightmax-height[right]   
                right-=1
        return t        
