# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    result = None
    while l1 and l2:
        l3 = ListNode((l1.val + l2.val + c) % 10)
        c = int((l1.val + l2.val + c) / 10)
        if result == None:
            result = l3;
        else:
            temp.next = l3;
        temp = l3;
        l1 = l1.next
        l2 = l2.next

    return result
            


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
