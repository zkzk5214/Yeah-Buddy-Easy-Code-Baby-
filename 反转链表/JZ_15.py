# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next: 
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next    # pHead.next is tmp(ex. 2)
            pHead.next = pre    # pHead.next aim to pre(ex. 1 -> None)
            pre = pHead         # pHead is pre(ex. 1 is pre)
            pHead = tmp         # tem is pHead
        return pre
