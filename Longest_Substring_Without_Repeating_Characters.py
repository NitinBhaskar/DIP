class Solution:
  def lengthOfLongestSubstring(self, s):
    substring = []
    max_len = 0
    for i in range(len(s)):
        if s[i] in substring:
            max_len = max(max_len, len(substring))
            substring.clear()
        else:
            substring.append(s[i])
    return max_len

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
