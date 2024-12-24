# 剑指 Offer 10- II. 青蛙跳台阶问题
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。


## Solution 1
## 跟斐波那契数列类似
## 每个台阶的跳法总和就是前一个台阶（跳一下）和前两个台阶（跳两阶）的跳法之和
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        dp = [1] * (n)
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]%1000000007


## Solution 2
## 改进版本solution，节省空间复杂度
## 每次迭代其实只需要前两个的数字即可
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
