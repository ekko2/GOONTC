# 23. 合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例1：
#
# 输入：lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# 输出：[1, 1, 2, 3, 4, 4, 5, 6]
# 解释：链表数组如下：
# [
#     1->4->5,
#           1->3->4,
#                 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例2：
#
# 输入：lists = []
# 输出：[]
# 示例
# 3：
#
# 输入：lists = [[]]
# 输出：[]
#
# 提示：
#
# k == lists.length
# 0 <= k <= 10 ^ 4
# 0 <= lists[i].length <= 500
# -10 ^ 4 <= lists[i][j] <= 10 ^ 4
# lists[i]按升序排列
# lists[i].length的总和不超过10 ^ 4




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for lst in lists:
            while lst:
                res.append(lst.val)
                lst = lst.next

        res.sort()
        dummy = ListNode(0)
        cur = dummy
        while res:
            cur.next = ListNode(res.pop(0))
            cur = cur.next
        return dummy.next