# 5.三数之和
# 给你一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c ，使得a + b + c = 0 ？请你找出所有和为0且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例1：
#
# 输入：nums = [-1, 0, 1, 2, -1, -4]
# 输出：[[-1, -1, 2], [-1, 0, 1]]
# 示例2：
#
# 输入：nums = []
# 输出：[]
# 示例3：
#
# 输入：nums = [0]
# 输出：[]
#
# 提示：
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums):
        def twoSum(nums, start, target, ans):
            lst = nums[start:]
            i = 0
            j = len(lst) - 1
            while i < j:
                if lst[i] + lst[j] > target:
                    j -= 1
                elif lst[i] + lst[j] < target:
                    i += 1
                else:
                    ans.add((nums[start - 1], lst[i], lst[j]))
                    i += 1

        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            twoSum(nums, i + 1, -nums[i], ans)
        return ans