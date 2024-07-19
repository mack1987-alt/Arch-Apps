import queue

# Create a priority queue
pq = queue.PriorityQueue()

# Add items to the queue with a priority number 
pq.put((1, 'task priority 1'))
pq.put((3, 'task priority 3'))
pq.put((2, 'task priority 2'))

# Retrieve items from the queue
while not pq.empty():
    priority, task = pq.get()
    print(f'Priority: {priority}, Task: {task}')