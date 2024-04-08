# Valid Parenthesess
# Given a string s containing only the characters '(', ')', '{', '}', '[', and ']', determine if it is a valid string.
#
# A string is considered valid if it meets the following conditions:
# 1. Open brackets ('(', '{', '[') must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every closing bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Explanation: The string contains a valid pair of parentheses.
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Explanation: The string contains valid pairs of parentheses, square brackets, and curly braces.
#
# Example 3:
#
# Input: s = "(]"
# Output: false
# Explanation: The string contains an invalid pair of parentheses, '(' is not properly closed.
#
# Constraints:
#
# - 1 <= s.length <= 10^4
# - The string s consists only of the characters '(', ')', '{', '}', '[', and ']'.
#
# TC: O(N)
# SC: O(N)

class Solution:
  def isValid(self, s: str) -> bool:
    st = []
    mp = dict({ ')': '(', '}': '{', ']': '[' })

    for c in s:
      if c in mp:
        if len(st) == 0 or st[-1] != mp[c]:
          return False
        else:
          st.pop()
      else:
        st.append(c)

    return len(st) == 0
