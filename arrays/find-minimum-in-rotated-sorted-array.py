# Find Minimum in Rotated Sorted Array
# Suppose you have an array of unique integers, initially sorted in ascending order. This array was rotated between 1 and n times, where n is the length of the array. For example:
# [4,5,6,7,0,1,2] is the result of rotating [0,1,2,4,5,6,7] four times.
# [0,1,2,4,5,6,7] remains the same after being rotated seven times.
# When an array is rotated once, the last element moves to the front. In general, rotating an array [a[0], a[1], a[2], ..., a[n-1]] one time results in [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given a sorted array that has been rotated, find the minimum element in the array.
#
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#
# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
#
# Constraints:
# The length of the array n is between 1 and 5000.
# All integers in the array are unique.
# The array is sorted and rotated between 1 and n times.
#
# TC: O(log(N))
# SC: O(1)

class Solution:
  def findMin(self, nums: List[int]) -> int:
    N = len(nums)

    l,r = 0, N-1
    mid = N//2
    while l <= r:
      mid = l + (r-l)//2

      if mid > 0 and nums[mid] < nums[mid-1]:
        break
      elif nums[mid] > nums[r]:
        l = mid+1
      else:
        r = mid-1

    mn = nums[0]
    if mid < N:
      mn = min(mn, nums[mid])

    return mn
