# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:42:32 2017

@author: Praveen S

https://leetcode.com/problems/combination-sum/#/description
"""

def combinationSum(candidates, target):
    """
    I shamelessly copied this from submitted solutions.
    But I got to learn about DFS and backtracking. Which is nice.
    
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    
    def dfs(index, target, path=[]):
        if target == 0:
            res.append(path)
            return
            
        for i in range(index, len(candidates)):
            if candy[i] > target: break
            dfs(i, target - candy[i], path + [candy[i]])
    
    res = []
    candidates.sort()            
    candy = candidates
    dfs(0,target,[])        
    return res                