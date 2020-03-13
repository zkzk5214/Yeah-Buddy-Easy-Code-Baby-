# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail1(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None
        # 设置两个指针，p2指针先走（k-1）步，然后再p1 p2一起走，当p2为最后一个时，p1为倒数第k个数
        p2 = head
        p1 = head
        # p2先走，走k-1步，如果k大于链表长度则返回 空，否则的话继续走
        while k > 1:
            if p2.next is not None:
                p2 = p2.next
                k -= 1
            else:
                return None
        # 两个指针一起 走，一直到p2为最后一个,p1即为所求
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        return p1

    def FindKthToTail2(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)    # 把head加入res的list中
            head = head.next    # 將下一個node設置為head
        if k > len(res) or k < 1:
            return
        return res[-k]  # 返回倒數第k個element
        # 列表切片
