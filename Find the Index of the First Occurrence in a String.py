class Solution(object):
    def strStr(self, haystack, needle):
        if not  needle:
            return -1
        if needle in haystack:
            return haystack.index(needle)    
        else:
            return -1    
