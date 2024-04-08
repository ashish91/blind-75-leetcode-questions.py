# Longest Repeating Character Replacement
# You are given a string s and a non-negative integer k. You can change at most k characters in the string s to any other uppercase English letter. Your goal is to find the length of the longest substring in s that contains the same letter after performing these operations.
#
# Examples:
#
# Input: A string s = "ABAB" and k = 2.
# You can replace both 'A's with 'B's or vice versa.
# The longest substring with the same letter would be "BBBB" of length 4.
# Input: A string s = "AABABBA" and k = 1.
# You can replace the middle 'A' with 'B', forming "AABBBBA".
# The longest substring with the same letter would be "BBBB" of length 4.
#
# Constraints:
# The length of s is between 1 and 105.
# s consists only of uppercase English letters.
# k is a non-negative integer between 0 and the length of s.

# TC: O(N)
# SC: O(1)
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    freq = [0]*26
    ord_A = ord('A')

    N = len(s)
    b, e = 0, 0
    mx = 0
    while e < N:
      freq[ord(s[e])-ord_A] += 1

      while e-b+1-max(freq) > k:
        freq[ord(s[b]) - ord_A] -= 1
        b += 1

      mx = max(mx, e-b+1)
      e += 1

    return mx
