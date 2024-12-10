class Solution(object):
    def maxArea(self, h):
        left=0
        right=len(h)-1
        maxi=0
        while left<right:
            curr=min(h[left],h[right])*(right-left)
            maxi=max(maxi,curr)
            if h[left]<h[right]:
                left+=1
            else:
                right-=1
        return maxi  
