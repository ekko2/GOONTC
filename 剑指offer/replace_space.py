# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

#  

# 示例 1：

# 输入：s = "We are happy."
# 输出："We%20are%20happy."


### solution 1
# 直接使用函数
class Solution_1:
    def replaceSpace(self, s):
        return s.replace(' ','20%')


### solution 2
# 变为list后插入再变为字符串

class Solution_2:
    def replaceSpace(self, s):
        lst = s.split(' ')
        return '%20'.join(lst)


### solution 3
# 一次遍历
class Solution_3:
    def replaceSpace(self, s):
        left = 0
        ans = ''
        for i in range(len(s)):
            if s[i] != ' ':
                ans += s[i]
            else:
                ans += '%20'
        
        return ans 


solution = Solution_3()
print(solution.replaceSpace("We are happy."))