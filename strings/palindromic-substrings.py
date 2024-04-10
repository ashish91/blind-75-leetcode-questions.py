# Palindromic Substrings
# Given a string s, find and return the number of palindromic substrings it contains.
#
# A string is considered a palindrome if it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
#
# Examples:
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic substrings: "a", "b", "c".
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
#
# TC: O(N)
# SC: O(N)
#

class Solution:
  def countSubstrings(self, s: str) -> int:
    def count_palindromes(b, e, s, N, palins):
      while b >= 0 and e < N:
        if s[b] != s[e]:
          break
        palins.add((b,e+1))
        b -= 1
        e += 1

      if b == -1 and e == N:
        palins.add((b+1,e))

    N = len(s)
    palins = set()
    for i in range(N):
      count_palindromes(i, i, s, N, palins)
      count_palindromes(i, i+1, s, N, palins)

    return len(palins)
