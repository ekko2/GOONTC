# 5. 最长回文子串
# 给你一个字符串s，找到s中最长的回文子串。
#
# 示例1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba"
# 同样是符合题意的答案。

# 示例2：
#
# 输入：s = "cbbd"
# 输出："bb"

# 示例3：
#
# 输入：s = "a"
# 输出："a"

# 示例4：
#
# 输入：s = "ac"
# 输出："a"
#
# 提示：
#
# 1 <= s.length <= 1000
# s
# 仅由数字和英文字母（大写和 / 或小写）组成

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def center(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1

        start, end = 0, 0
        for i in range(len(s)):
            len1 = center(i, i)
            len2 = center(i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > end - start + 1:
                start = i - (maxlen - 1) // 2

                end = i + maxlen // 2

        return s[start:end + 1]