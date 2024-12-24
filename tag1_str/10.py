# 19.
# 删除链表的倒数第N个结点
# 给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。
#
# 进阶：你能尝试使用一趟扫描实现吗？
#
# 示例1：
#
#
# 输入：head = [1, 2, 3, 4, 5], n = 2
# 输出：[1, 2, 3, 5]

# 示例2：
#
# 输入：head = [1], n = 1
# 输出：[]

# 示例3：

#
# 输入：head = [1, 2], n = 1
# 输出：[1]
#
# 提示：
#
# 链表中结点的数目为
# sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        for i in range(n):
            slow = slow.next

        if not slow:
            head = head.next
            return head

        while slow.next:
            fast = fast.next
            slow = slow.next

        fast.next = fast.next.next

        return head