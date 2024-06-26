# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
#
# Solve this problem in O(1) space. (Output array does not count in space complexity.)
#
# TC: O(N)
# SC: O(1)
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    N = len(nums)
    l = [1]*N

    for i in range(1,N):
      l[i] = l[i-1] * nums[i-1]

    rval = 1
    for i in range(N-2,-1,-1):
      rval = rval * nums[i+1]
      l[i] *= rval

    return l
