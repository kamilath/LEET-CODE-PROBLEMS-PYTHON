class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2[:n]
        return nums1.sort()
