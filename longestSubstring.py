# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:24:52 2017

@author: subramanian-p
"""

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        length = 0
        longestString = ""
        for x in s:
            if x not in st:
                st.append(x)
                longestString = "".join(st)
                #print("A",x)
            else:
                if st[-1] == x:
                    length = max(length, len(st))
                    #print("B",length,st,x)
                    st = []
                    st.append(x)
                else:
                    length = max(length, len(st))
                    st = st[st.index(x) + 1 :]
                    st.append(x)
                    longestString = "".join(st)
                    #print("C",length,st,x)
        print(longestString)
        return max(length,len(st))