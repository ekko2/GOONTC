# 剑指 Offer 07. 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# 示例 1:



# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder) :
        n = len(inorder)
        if n == 0:
            return None
        val = preorder[0]
        index = inorder.index(val)
        root = TreeNode(val)
        left_in = inorder[:index]
        left_pr = preorder[1:index+1]
        right_in = inorder[index+1:]
        right_pr = preorder[index+1:]
        root.left = self.buildTree(left_pr,left_in)
        root.right = self.buildTree(right_pr,right_in)
        
        return root