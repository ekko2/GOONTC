# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

# 你可以按任意顺序返回答案。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/two-sum

class Solution_1():
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []

class Solution_2():
    def twoSum(self,nums,target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            dic[target - nums[i]] = i

        dic = {}
        for i in len(nums):
            if nums[i] not in dic:
                dic[target-nums[i]] = i
            else:
                return [dic[nums[i]], i]