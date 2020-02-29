# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, ListNode):
        if not ListNode:
            return []
        result = []
        head = ListNode

        while head:
            result.insert(0, head.val)  # insert start at head
            head = head.next
        return result
