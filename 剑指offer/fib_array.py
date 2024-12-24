# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



## Solution 1 
## 递归解法，一般会超时，时间复杂度极大



## Solution 2 
## 最简单DP， 已给转移方程的DP题目
## 新建一个array，将转移方程直接输入就行
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]%1000000007