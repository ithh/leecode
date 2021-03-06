#!/usr/bin/python3
# -*- encoding: utf-8 -*-


'''
File    :   3.py
Time    :   2020/10/23 11:05:19
Author  :   ithh 
Version :   1.0
Contact :   hhxhwxh@qq.com
Desc    :   None
'''

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

思路：滑动窗口
例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
如何移动？
我们只要把队列的左边的元素移出就行了，直到满足题目要求！
一直维持这样的队列，找出队列出现最长的长度时候，求出解！
时间复杂度：O(n)O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len

# hash表实现
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,res,newdic=-1,0,{}
        for i,c in enumerate(s):#按循环顺序，把s中的元素挨个放到新的newdic里去
            if c in newdic and newdic[c]>start:
                start=newdic[c]#重新定位start指针
                newdic[c]=i#给这个重复字母赋上顺序值
            else:#newdic里还没有这个重复字母，且不需要重新定位指针（重复字母在start之前，说明已经算过了，略掉）
                    newdic[c]=i
                    res=max(res,i-start)   #更新最大子串长度   
        return res