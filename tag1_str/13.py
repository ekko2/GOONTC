# 22.
# 括号生成
# 数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
#
# 有效括号组合需满足：左括号必须以正确的顺序闭合。
#
#
#
# 示例1：
#
# 输入：n = 3
# 输出：["((()))", "(()())", "(())()", "()(())", "()()()"]
# 示例2：
#
# 输入：n = 1
# 输出：["()"]
#
# 提示：
#
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, cur, res):
            if l == n and r == n:
                res.append(cur)
                return
            if l < n:
                dfs(l + 1, r, cur + '(', res)
            if r < n and r < l:
                dfs(l, r + 1, cur + ')', res)

        res = []
        dfs(0, 0, '', res)
        return res