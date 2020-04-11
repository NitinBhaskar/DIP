class Solution:
  def isValid(self, s):
    paran_dict = {'(':')', '{':'}', '[':']'}
    paran_stack = []
    if s == "":
        return True

    for i in range(len(s)):
        if s[i] in paran_dict.keys():
            paran_stack.append(s[i])
        else:
            c = paran_dict[paran_stack.pop()]
            if s[i] != c:
                return False

    if len(paran_stack) > 0:
        return False

    return True
    

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
