# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:03:25 2017

@author: Praveen S

https://leetcode.com/problems/merge-two-sorted-lists
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = res = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            
            res = res.next
        
        res.next = l1 or l2
        
        return root.next
        
                    
            
        