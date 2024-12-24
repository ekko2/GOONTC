# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/add-two-numbers


# https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Solution 1
## 直接将两个链表转换为list
class Solution():
    def addnumber(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1+=str(l1.val)
            l1 = l1.next
        while l2:
            num2+=str(l2.val)
            l2 = l2.next

        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        
        res = num1+num2
        res = str(res)[::-1]
        
        x = ListNode(int(res[0]))
        dummy = x
        for i in range(1,len(res)):
            x.next = ListNode(x[i])
        
        return dummy
        

## Solution 2
## 可以对每个链表的数字操作，进位则nextnode val+1
        

        