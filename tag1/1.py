# 1.
# 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
# 示例1：
#
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为nums[0] + nums[1] == 9 ，返回[0, 1] 。
#
# 示例2：
#
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
#
# 示例3：
#
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]
#
# 提示：
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
# 进阶：你可以想出一个时间复杂度小于O(n2) 的算法吗？

#
# 解法1
# 1. 暴力解法 直接遍历两遍找两数之和
class Solution_1():
    def twoSum(self, nums: [], target: int):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []

# 2. hashtable
class Solution_2():
    def twoSum(self, nums: [], target: int):
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target-nums[i]] = i
            else:
                return [dic[nums[i]],i]





