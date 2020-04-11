class Solution: 
  def getRange(self, arr, target):
    start = 0
    end = 0
    i = 0
    if target not in arr:
        return [-1, -1]
    while arr[i] != target:
        i += 1
        if i == len(arr):
            break

    if i != len(arr):
        start = i

    while arr[i] == target:
        i += 1
        if i == len(arr):
            break

    if i != len(arr):
        end = i - 1

    return [start, end]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
#Output: [6,8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
#Output: [1,2]

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
#Output: [-1, -1]
