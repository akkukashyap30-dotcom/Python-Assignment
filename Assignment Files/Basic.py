print("My Name is Akash Kumar")

# This is a single-line comment
print("Hello, Python")

"""
This is a multi-line comment.
# It can be used to explain
# multiple lines of code.
"""
print("Comments example")

num = 10

# Boolean
is_active = True

# Character (Python does not have char type, it uses string)
char = 'A'

# float
price = 25.5

distance = 123.456789

print("Integer:", num)
print("Boolean:", is_active)
print("Character:", char)
print("Float:", price)
print("Double:", distance)

a = 100   # Global variable

def demo():
    a = 50   # Local variable
    print("Local variable a:", a)

demo()
print("Global variable a:", a)