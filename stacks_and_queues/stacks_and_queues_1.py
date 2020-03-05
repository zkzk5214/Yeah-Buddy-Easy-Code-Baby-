# Consider a stack of letters:
letters = []

# Push some letters into list
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

# Pop letters, get 'g'
last_item = letters.pop()
print(last_item)    # g

# Pop again, get 't'
last_item = letters.pop()
print(last_item)    # t

# 'c' and 'a' remain
print(letters)      # ['c','a']
