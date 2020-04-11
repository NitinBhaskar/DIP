class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    if head is None or head.next is None:
        return head
    curr = head.next
    prev = head
    head.next = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    head = prev
    return head

  # Recursive Solution      
  def reverseRecursively(self, head):
    def reverse_util(curr):
        global new_head
        if curr.next is None:
            new_head = curr
            return curr
        else:
            temp = reverse_util(curr.next)
            temp.next = curr
            curr.next = None
            return curr

    if head is None or head.next is None:
        return head
    reverse_util(head)
    return new_head

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#testHead = testHead.reverseIteratively(testHead)
testHead = testHead.reverseRecursively(testHead)
print("List after reversal: ")
testHead.printList()
# 0 1 2 3 4

