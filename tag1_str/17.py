# 38. 外观数列
# 给定一个正整数 n ，输出外观数列的第 n 项。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

# 你可以将其视作是由递归公式定义的数字字符串序列：

# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

# 前五项如下：

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1 
# 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
# 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
# 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
# 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"



###  Solution 1
###  简单递归，每次递归一下
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '11'
        x = str(self.countAndSay(n-1))
        cur = x[0]
        count = 1
        res = ''
        for i in range(1,len(x)):
            if cur != x[i]:
                res += str(count) + cur

                cur = x[i]
                count = 1
            count += 1

        res += str(count) + cur
        return res            



###  Solution2
###  有点像DP的双指针，对n以内的每个数都按题目意思计算一遍，然后不停迭代res这个结果。

class Solution:
    def countAndSay(self, n):
        res = '1'
        for i in range(n-1):
            cur = res[0]
            count = 0
            ans = ''
            for j in range(1,len(res)):
                cur = res[j]
                if res[i] != cur:
                    ans += str(count) + str(prev)
                    prev = cur  
                    count = 0
                count += 1
            res = ans+str(count) + str(prev)
        
        return res

