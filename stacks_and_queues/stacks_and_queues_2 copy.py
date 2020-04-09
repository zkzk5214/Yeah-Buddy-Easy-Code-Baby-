# Consider a queue of fruits
fruits = []

# Enqueue some fruits into our list
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

# Dequeue fruits, get 'banana'
first_item = fruits.pop(0)
print(first_item)

# Dequque again, get 'grapes'
first_item = fruits.pop(0)
print(first_item)

# 'mango' and 'orange' remain
print(fruits)  # ['mango','orange']
