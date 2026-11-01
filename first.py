string = input("enter your sentense:")
stack = []
for char in string:
    stack.append(char)
reversed_str = ""
while stack:
    reversed_str+=stack.pop()

print(reversed_str)