# Group Anagrams
# Given an array of strings strs, group the strings that are anagrams of each other together.
# An anagram is a word formed by rearranging the letters of another word,
# using all the original letters exactly once. Return the grouped anagrams in any order.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
# TC: O(NWlog(W))
# SC: O(NW)
#
# N words, W max length word

from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)

    # O(N)
    for w in strs:
      # O(Wlog(W))
      s = ''.join(sorted(w))
      ans[s].append(w)

    return list(ans.values())
