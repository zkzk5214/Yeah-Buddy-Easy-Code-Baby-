from collections import deque

# Initialize a deque with a list
numbers = deque()
# Use append to add elements
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

# pop like a stack
last_item = numbers.pop()
print(last_item)    # 47
print(numbers)      # deque([99, 15, 82, 50])

# pop like a queue
first_item = numbers.popleft()
print(first_item)   # 99
print(numbers)      # deque([15, 82, 50])
