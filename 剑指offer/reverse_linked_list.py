# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

#  

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


### Solution 1
# 先转换成list，再转换成listnode
class Solution_1:
    def reverseList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        res = res[::-1]
        new = ListNode(res[0])
        dummy = new
        for i in range(1,len(res)):
            new.next = ListNode(res[i])
            new = new.next
        
        return dummy


### Solution 2
# 反转链表，定义一个prev node
class Solution_1:
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            
            prev = head
            head = temp
            
        
        return prev