def check1(Str):
    # Function to check parentheses
    stack = []
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    for i in Str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                # {[] --> index of ] corresponding to [ in open_list == [ (former one in stack)
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


def check2(Str):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))    # {'(': ')', '{': '}', '[': ']'}
    queue = []
    for i in Str:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    return "Balanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check1(string))

string = "[{}{})(]"
print(string, "-", check2(string))
