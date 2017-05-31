# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:36:48 2017

@author: Praveen

Find all possible permutations of a string
"""

def swap(list, a, b):
    list[a],list[b] = list[b],list[a]
    
def permutations(list,start,end):
    if start == end:
        print('I',list)
        return
    for j in range(start, end):
        swap(list,j,start)
        permutations(list,start+1,end)
        swap(list,start,j)
        
def main():
    lst = list("praveen")
    start = 0
    end = len(lst)
    permutations(lst,start,end)
    
main()