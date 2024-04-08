# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# Follow-up: Can you solve this problem in linear time and constant space?

# TC: O(N)
# SC: O(1)
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    mx = 0
    mxval = nums[0]

    curr = 0
    for v in nums:
      mxval = max(mxval, v)

      curr += v
      if curr < 0:
        curr = 0
      mx = max(mx, curr)

    return mx if mx != 0 else mxval
