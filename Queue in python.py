'''
q=[]
q.append(5)
q.append(10)
q.append(15)

print(q)
   
print(q.pop(0))
print(q.pop(0))
print(q)

queue = []            # initialize empty queue
MAX_SIZE = 5          # optional size limit

# -------- Enqueue (Push) --------
if len(queue) < MAX_SIZE:
    queue.append("A")
    print("Enqueued: A")
else:
    print("Queue Overflow!")

if len(queue) < MAX_SIZE:
    queue.append("B")
    print("Enqueued: B")
else:
    print("Queue Overflow!")

if len(queue) < MAX_SIZE:
    queue.append("C")
    print("Enqueued: C")
else:
    print("Queue Overflow!")

print("Queue after enqueue operations:", queue)

# -------- Dequeue (Pop) --------
if len(queue) > 0:
    removed = queue.pop(0)
    print("Dequeued:", removed)
else:
    print("Queue Underflow!")

if len(queue) > 0:
    removed = queue.pop(0)
    print("Dequeued:", removed)
else:
    print("Queue Underflow!")

print("Queue after dequeue operations:", queue)
n=int(input())
sum=0
for i in range(1,11):
    sum+=n*i
    i+=1
    print(sum)
n=int(input())
sum=0
for i in range(1,11):
    if i %2==0:
        sum+=n*i
        i+=1
    print(sum)

n=int(input())
sum=0
for i in range(1,11):
    if i %2==1:
        sum+=n*i
        i+=1
    print(sum)

n=int(input())
sum=0
for i in range(1,11):
    if i%3!=0:
        sum+=n*i
        i+=1
    print(sum)
'''
nums=list(range(100,0-1))
total=0
for i in range(0,len(nums),2):
    print(nums[i],end=" ")
    total +=nums[i]
print("\n sum :",total)