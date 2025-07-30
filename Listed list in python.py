class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
#
class node:
    def __init__(self, data):
        self.data = data
        self.next = None           
n1 = node(10)
n2 = node(20)
n3 = node(10)

n1.next = n2
n2.next = n3                   
n3.next = None

head = n1


newnode = node(30)
newnode.next = head
head = newnode

value=20
if head is not None and head.data == value:
    head= head.next
else:
    current=head
    while current.next is not None:
        if current.next.data==value:
            current.next=current.next.next
            break
        current=current.next


current = head
while current is not None:
    print(current.data, end=",")
    current = current.next
print("None")
#
#Single linked list
#
class node:
    def __init__(self, data):
        self.data = data
        self.next = None           

# Step 1: Create initial list: 10 → 20 → 10
n1 = node(10)
n2 = node(20)
n3 = node(10)

n1.next = n2
n2.next = n3                   
n3.next = None
head = n1

# INSERTION AT START
newnode_start = node(30)
newnode_start.next = head
head = newnode_start

# INSERTION AT END
newnode_end = node(40)
current = head
while current.next is not None:
    current = current.next
current.next = newnode_end

#  DISPLAY BEFORE DELETION
print("Before deletion:")
current = head
while current is not None:
    print(current.data, end=" → " if current.next else "")
    current = current.next
print("None")

# DELETION AT START
if head is not None:
    head = head.next

# DELETION AT END
if head is None:
    pass
elif head.next is None:
    head = None
else:
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None

# DISPLAY AFTER DELETION
print("After deletion:")
current = head
while current is not None:
    print(current.data, end=" → " if current.next else "")
    current = current.next
print("None")

