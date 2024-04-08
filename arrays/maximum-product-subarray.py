# Maximum Product Subarray
# Given an integer array nums, find a contiguous subarray within the array that has the largest product of its elements, and return that product.
# The test cases are designed so that the result will fit within a 32-bit signed integer.
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: The subarray [2,3] has the largest product, which is 6.
#
# Example 2:
#
# Input: nums = [0, 2, -3, 4, -5]
# Output: 120
# Explanation: The subarray [2, -3, 4, -5] has the largest product of 120.
#
# Example 3:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The subarray [-2,0] or [-1] does not have a positive product, so the largest product is 0.
#
# Constraints:
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
#
# NB: The product of any prefix or suffix of nums is guaranteed to fit within a 32-bit signed integer.
# Follow up: Solve this problem in linear time and constant space.
