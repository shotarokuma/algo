class Node:
  def __init__(self, val = None):
    self.val = val
    self.nextval = None

class LinkedList:
  def __init__(self):
    self.head = None

list = LinkedList()
list.head = Node(1)
list.head.nextval = Node(2)

print(list.head.val)

list = list.head.nextval

print(list.val)