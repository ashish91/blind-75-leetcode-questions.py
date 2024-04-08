# Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#
# TC: O(M+N)
# SC: O(1)

from collections import defaultdict

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
      return ""

    freq = [0]*128
    b = e = 0
    b_ind = 0
    min_len = float('infinity')
    N = len(s)
    chars_left = len(t)

    for c in t:
      freq[ord(c)] += 1

    while e < N:
      while e < N and chars_left > 0:
        if freq[ord(s[e])] > 0:
          chars_left -= 1
        freq[ord(s[e])] -= 1
        e += 1

      while chars_left == 0:
        if e-b < min_len:
          min_len = e-b
          b_ind = b

        if freq[ord(s[b])] == 0:
          chars_left += 1

        freq[ord(s[b])] += 1
        b += 1

    if min_len == float('infinity'):
      return ""
    else:
      return s[b_ind:b_ind+min_len]
