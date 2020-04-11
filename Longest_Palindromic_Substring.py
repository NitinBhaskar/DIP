class Solution: 
    def longestPalindrome(self, s):
      for i in range(len(s)):
          print(i)
          print(len(s) - i)
          substring = s[i: len(s) - i]
          if substring == "".join(reversed(substring)):
              return substring
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
