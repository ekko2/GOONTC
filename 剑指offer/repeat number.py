# 重复数字

# 找出数组中重复的数字。


# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
# 但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

# 示例 1：

# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 



## Solution 1
## 排序整个数组，从头到尾扫描一整个数组











class Solution_1:
    def findRepeatNumber(self, nums):
        new_nums = sorted(nums)
        for i in range(len(new_nums)):
            if new_nums[i] != i:
                return i


## Solution 2
## 哈希表

class Solution_1:
    def findRepeatNumber(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return i



## Solution 3
## sort 方式
## 扫描整个数组，扫描到index = i的时候，比较index = i的数字是否=i，如果相等，就继续扫描。如果不相等，就将index = m的数字与m比较
## 若如果和第m的数字相等，那就找到了该数字，否则就交换，将m放到适合他的位置

class Solution_3:
    def findRepeatNumber(self, nums):
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            
            else:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    nums[nums[i]] = temp
                    nums[i] = nums[nums[i]]

# solution = Solution_3()
# nums = [2, 3, 1, 0, 2, 5, 3]
# res = solution.findRepeatNumber(nums)
# print(res)
        
        
    

## Solution 4
## 二分查找

class Solution_4:
    def findRepeatNumber(self, nums):
        lens = len(nums)
        for i in range(len(nums)):
            