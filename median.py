# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:32:45 2017

@author: subramanian-p
"""

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    
    merged = nums1 + nums2
    merged.sort()
    middle = len(merged)/2
    
    if len(merged) % 2 > 0:
        return float(merged[middle])
    
    return float((merged[middle-1] + merged[middle]) / 2.0)
    
    
    
    