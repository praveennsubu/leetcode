# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:23:55 2017

@author: subramanian-p
"""

def reverseInt(x):
    multiplier = 1
    if x < 0:
        multiplier = -1

    ans = 0
    div = x * multiplier
                
    while(div > 0):
        div, mod = divmod(div, 10)
        ans = (ans * 10) + mod
    print(ans * multiplier)
    if (ans > 2147483647):
        return 0
    return ans * multiplier
    