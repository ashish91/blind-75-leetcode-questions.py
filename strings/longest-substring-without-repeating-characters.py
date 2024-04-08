# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# TC: O(N)
# SC: O(1)
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    d = set()

    N = len(s)
    b, e = 0, 0

    mx = 0
    while e < N:
      v = s[e]
      while v in d:
        d.remove(s[b])
        b += 1

      d.add(v)
      mx = max(mx, e-b+1)
      e += 1

    return mx
