class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create initial circular linked list: 10 → 20 → 30 → back to 10
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3
n3.next = n1  

head = n1

# Insertion at specific position
position = 2          
new_data = 15      
new_node = Node(new_data)

if position == 1:
    temp = head
    while temp.next != head:
        temp = temp.next  
    temp.next = new_node
    new_node.next = head
    head = new_node
else:
    current = head
    count = 1
    while count < position - 1 and current.next != head:
        current = current.next
        count += 1
    new_node.next = current.next
    current.next = new_node

# Print list after insertion
print("After Insertion at Position", position)
temp = head
while True:
    print(temp.data, end=" → ")
    temp = temp.next
    if temp == head:
        break
print("(back to start)")

# Deletion at specific position
delete_pos = 2
if head is None:
    print("List is empty")
elif delete_pos == 1:
    temp = head
    last = head
    while last.next != head:
        last = last.next
    if head.next == head:
        head = None
    else:
        head = head.next
        last.next = head
else:
    current = head
    count = 1 
    while count < delete_pos - 1 and current.next != head:
        current = current.next
        count += 1
    if current.next == head or current.next == None:
        print("Invalid position")
    else:
        current.next = current.next.next

# Print list after deletion
if head:
    print("After Deletion at Position", delete_pos)
    t = head
    while True:
        print(t.data, end=" → ")
        t = t.next
        if t == head:
            break
    print("(back to start)")
else:
    print("List is now empty")
