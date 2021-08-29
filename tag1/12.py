# 21.合并两个有序链表
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例1：
#
#
# 输入：l1 = [1, 2, 4], l2 = [1, 3, 4]
# 输出：[1, 1, 2, 3, 4, 4]

# 示例2：
#
# 输入：l1 = [], l2 = []
# 输出：[]

# 示例3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
# 提示：
#
# 两个链表的节点数目范围是[0, 50]-100 <= Node.val <= 100
# l1和l2均按非递减顺序排列
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            x = l1.val if l1 else float('inf')
            y = l2.val if l2 else float('inf')
            if x >= y:
                cur.next = l2
                if l2:
                    l2 = l2.next
                else:
                    l2 = float('inf')
            else:
                cur.next = l1
                if l1:
                    l1 = l1.next
                else:
                    l1 = float('inf')

            cur = cur.next

        return dummy.next