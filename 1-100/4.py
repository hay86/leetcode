class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1) + len(nums2)
        if k % 2 == 0:
            return (self.kth(nums1, nums2, k/2-1) + self.kth(nums1, nums2, k/2))/2.
        else:
            return self.kth(nums1, nums2, k/2)
    
    def kth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.kth(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        p1 = min(k/2, len(nums1)-1)
        p2 = k-p1-1
        if nums1[p1] == nums2[p2]:
            return nums1[p1]
        elif nums1[p1] > nums2[p2]:
            return self.kth(nums1, nums2[p2+1:], k-p2-1)
        else:
            return self.kth(nums1[p1+1:], nums2, k-p1-1)
            
        
