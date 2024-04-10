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
# TC: O(N^2)
# SC: O(1)
#

class Solution:
  def countSubstrings(self, s: str) -> int:
    def count_palindromes(b, e, s, N):
      cnt = 0
      while b >= 0 and e < N:
        if s[b] != s[e]:
          return cnt
        cnt += 1
        b -= 1
        e += 1

      return cnt


    N = len(s)
    total = 0
    for i in range(N):
      total += count_palindromes(i, i, s, N)
      total += count_palindromes(i, i+1, s, N)

    return total
