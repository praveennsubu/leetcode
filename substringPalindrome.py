# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:56:13 2017

@author: subramanian-p
"""

def substrPalin(s):
    visited = {}
    
    if(len(s) == 0): return ""
    
    longestPalin = s[0]
    
    #if(len(s) == 1): return s
    #
    
    for i in range(len(s)):
        if s[i] not in visited:
            indexes = set()
            indexes.add(i)
            visited[s[i]] = indexes
        else:
            indexes = visited[s[i]]
            indexes.add(i)
            substr = [s[ind:i + 1] for ind in indexes
                      if len(s[ind:i + 1]) > len(longestPalin)]
            palins = {palin:len(palin) for palin in substr 
                      if palin == palin[::-1]}
            if palins:
                longestPalin = max(palins)

    return longestPalin