class Solution(object):
    def maxArea(self, h):
        l=0
        r=len(h)-1
        water=0
        while l<r:
            water=max(water,(r-l)*min(h[l],h[r]))
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return  water  
