# 32. 最长有效括号
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

# 示例 1：

# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：

# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：

# 输入：s = ""
# 输出：0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res,i-stack[-1])
                else:
                    stack.append(i)
        
        return res