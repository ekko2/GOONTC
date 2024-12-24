# 4. 寻找两个正序数组的中位数
# 给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数 。
#

# 示例1：
#
# 输入：nums1 = [1, 3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1, 2, 3] ，中位数2

# 示例2：
#
# 输入：nums1 = [1, 2], nums2 = [3, 4]
# 输出：2.50000
# 解释：合并数组 = [1, 2, 3, 4] ，中位数(2 + 3) / 2 = 2.5

# 示例3：
#
# 输入：nums1 = [0, 0], nums2 = [0, 0]
# 输出：0.00000

# 示例4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000

# 示例5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
# 提示：
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2**40
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        median1, median2 = 0, 0

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1
