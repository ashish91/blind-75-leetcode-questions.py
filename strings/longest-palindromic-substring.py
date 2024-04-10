# Longest Palindromic Substring
# Given a string s, find and return the longest palindromic substring within s.
#
# Examples:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid palindromic substring.
#
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists only of digits and English letters.
#
# TC: O(N)
# SC: O(1)

class Solution:
  def longestPalindrome(self, s: str) -> str:
    def max_palindrome(b, e, s, N):
      while b >= 0 and e < N:
        if not s[b].isalnum() or not s[e].isalnum() or s[b] != s[e]:
          return [e-b, s[b+1:e]]
        b -= 1
        e += 1

      return [e-b, s[b+1:e]]

    N = len(s)
    if N < 2:
      return s

    mx = 0
    mxlen = 0
    for i in range(N):
      olen, odd_palin = max_palindrome(i, i, s, N)
      if olen > mxlen:
        mxlen = olen
        mx = odd_palin

      elen, even_palin = max_palindrome(i, i+1, s, N)
      if elen > mxlen:
        mxlen = elen
        mx = even_palin
    return mx
