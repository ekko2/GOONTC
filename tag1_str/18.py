# 43. 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

 

# 示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
 

 ### 反向摆竖式
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        sums = [0] * (len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(nums2)): 
                sums[i+j] += int(num1[i])*int(num2[j])
        carry = 0
        ans = ''
        for i in range(len(sum)):
            x  = (sums[i] + carry) % 10
            carry = (sums[i] + carry) //10
            ans = str(x) + ans
        
        while ans[0] == '0' and len(ans) >= 2:
            ans = ans[1:]
        return ans
