# https://github.com/badprog/badprog_leetcode_python

from typing import List, Tuple

############################
#
class Solution:
    ############################
    #
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 must have the lesser or equal length compared to nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 # swap
        m, n = len(nums1), len(nums2) # define m and n
        left, right = 0, m

        # Loop 
        while left <= right:
            i = (left + right) // 2     # i for nums1 (left1 and right1)
            j = (m + n + 1) // 2 - i    # j for nums2 (left2 and right2)

            # check
            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # final check 
            if left1 <= right2 and left2 <= right1:
                # we can get the median
                if (m + n) % 2 == 1:
                    return max(left1, left2) # odd
                return (max(left1, left2) + min(right1, right2)) / 2 # even
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("Lists not sorted or invalid")

