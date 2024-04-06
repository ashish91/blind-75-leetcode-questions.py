# Contains Duplicate
# For a given array of integers, nums, return true if it contains duplicates. Otherwise, return false.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# TC: O(N)
# SC: O(N)
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    presence = set()

    for v in nums:
      if v in presence:
        return True
      presence.add(v)

    return False
