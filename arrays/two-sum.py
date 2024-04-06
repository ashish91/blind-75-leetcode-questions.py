# Two Sum
# You are given an array of integers nums and an integer target.
# Your task is to find two distinct indices i and j such that
# the sum of nums[i] and nums[j] is equal to the target.
# You can assume that each input will have exactly one solution, and you may not use the same element twice.
#
# NB:  Assume the input array contains valid pair and return the pair as sorted.
#
# Example 1:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Explanation: nums[1] + nums[2] gives 2 + 4 which equals 6.
#
# Example 2:
#
# Input: nums = [-1, -2, -3, -4, -5], target = -8
# Output: [2, 4]
# Explanation: nums[2] + nums[4] yields -3 + (-5) which equals -8.
#
# Example 3:
#
# Input: nums = [10, 15, 20, 25, 30], target = 45
# Output: [1, 3]
# Explanation: nums[1] + nums[3] gives 15 + 30 which equals 45.

# Solution using external memory
# TC: O(N)
# SC: O(N)
class Solution:
  def twoSum(self, nums: List[int], sum: int) -> List[int]:
    freq = dict()

    N = len(nums)
    for i in range(N):
      if nums[i] in freq:
        freq[nums[i]].append(i)
      else:
        freq[nums[i]] = [i]

    for i in range(N):
      oth = sum - nums[i]

      if oth in freq:
        if nums[i] == oth:
          if len(freq[oth]) > 1:
            return freq[oth][0:2]
        else:
          return [freq[oth][0], i]

    return []
