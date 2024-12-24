# 31.下一个排列
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
#
#
# 示例1：
#
# 输入：nums = [1, 2, 3]
# 输出：[1, 3, 2]
# 示例2：
#
# 输入：nums = [3, 2, 1]
# 输出：[1, 2, 3]
# 示例3：
#
# 输入：nums = [1, 1, 5]
# 输出：[1, 5, 1]
# 示例4：
#
# 输入：nums = [1]
# 输出：[1]
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mark = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                mark = i
                break
        print(mark)
        if mark != 0:
            for i in range(len(nums) - 1, mark - 1, -1):
                if nums[mark - 1] < nums[i]:
                    nums[mark - 1], nums[i] = nums[i], nums[mark - 1]
                    break

        nums[mark:] = nums[mark:][::-1]