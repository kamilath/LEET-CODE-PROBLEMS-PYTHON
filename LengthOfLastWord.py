class Solution(object):
    def lengthOfLastWord(self, s):
        s1=s.strip().split()
        s2=s1[-1]
        return len(s2)
        
