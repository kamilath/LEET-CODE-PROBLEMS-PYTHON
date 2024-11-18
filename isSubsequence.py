class Solution(object):
    def isSubsequence(self, s, t):
        s1=0
        for i in t:
            if s1<len(s) and s[s1]==i:
                s1+=1
        return s1==len(s) 
