# A simple class stack that only allows pop and push operations
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peak(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


document_actions = Stack()

# The first enters the title of the document
document_actions.push('action: enter; text_id: 1; text: This is my favourite document')
# Next center the text
document_actions.push('action: format; text_id: 1; alignment: center')
# As with most writers, the user is unhappy with the first draft and undoes the center alignment
document_actions.pop()
# The title is better on the left with bold font
document_actions.push('action: format; text_id: 1; style: bold')

##
input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('DOWN')
input_queue.enqueue('RIGHT')
input_queue.enqueue('B')

# Now we can process each item in the queue by dequeueing them
key_pressed = input_queue.dequeue()  # 'DOWN'

# We'll probably change our player position
key_pressed = input_queue.dequeue()  # 'RIGHT'

# We'll change the player's position again and keep track of a potential special move to perform
key_pressed = input_queue.dequeue()  # 'B'

# This can do the act, but the game's logic will know to do the special move
