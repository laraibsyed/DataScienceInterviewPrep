class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge and sort the two arrays
        merged = sorted(nums1 + nums2)
        
        # Calculate the length of the merged array
        length = len(merged)
        
        # Find the median
        if length % 2 != 0:
            # Odd length: Return the middle element
            median = merged[length // 2]
        else:
            # Even length: Return the average of the two middle elements
            mid1 = length // 2
            mid2 = mid1 - 1
            median = (merged[mid1] + merged[mid2]) / 2.0  # Ensure result is a float
        
        return median
