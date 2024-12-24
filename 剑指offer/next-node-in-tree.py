# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。



# 中序遍历 左根右
# 前序遍历 根左右
# 后序遍历 左右根
# 因此，中序遍历的当前节点的下一个节点只有三种可能
# 1. 该结点有右子树，则该结点的下一个结点是其右子树的最左结点
# 2. 若该结点没有右子树，且该结点是其父结点的左孩子，则该结点的下一个结点是其父结点
# 3. 若该结点没有右子树，则一直往父结点的方向上寻找，直到找到某一个结点是其父结点的左子树，则证明这棵子树遍历完了，这个结点的父结点就是所要求的结点。

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:    return None
        
        # 若该结点有右子树，则该结点的下一个结点是其右子树的最左结点
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        
        # 若该结点没有右子树，且该结点是其父结点的左孩子，则该结点的下一个结点是其父结点
        if pNode.next and pNode.next.left == pNode:
            return pNode.next
        
        # 若该结点没有右子树，则一直往父结点的方向上寻找，直到找到某一个结点是其父结点的左子树，这个结点的父结点就是所要求的结点。
        else:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            return None
