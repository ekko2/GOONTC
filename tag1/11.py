# 20.有效的括号
# 给定一个只包括'('，')'，'{'，'}'，'['，']'的字符串s ，判断字符串是否有效。
#
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 示例1：
#
# 输入：s = "()"
# 输出：true

# 示例2：
#
# 输入：s = "()[]{}"
# 输出：true

# 示例3：
#
# 输入：s = "(]"
# 输出：false

# 示例4：
#
# 输入：s = "([)]"
# 输出：false

# 示例5：
#
# 输入：s = "{[]}"
# 输出：true
#
# 提示：
#
# 1 <= s.length <= 104
# s仅由括号'()[]{}'组成

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
                continue

            if not stack:
                return False

            if dic[i] != stack[-1]:
                return False

            else:
                stack.pop(-1)

        if stack:
            return False
        return True