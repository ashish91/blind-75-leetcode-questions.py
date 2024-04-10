# Valid Palindrome
# Given a string s, determine if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters. A palindrome is a phrase that reads the same forwards and backwards.
#
# Examples:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: After converting to lowercase and removing non-alphanumeric characters, "amanaplanacanalpanama" reads the same forward and backward.
#
# Input: s = "race a car"
# Output: false
# Explanation: After processing, "raceacar" is not a palindrome.
#
# Input: s = " "
# Output: true
# Explanation: The empty string "" after processing is considered a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
# TC: O(N)
# SC: O(1)

class Solution:
  def isPalindrome(self, s: str) -> bool:
    N = len(s)

    b, e = 0, N-1

    while b < e:
      while b < e and not s[b].isalnum():
        b += 1
      while b < e and not s[e].isalnum():
        e -= 1

      if s[b].lower() != s[e].lower():
        return False

      b += 1
      e -= 1

    return True
