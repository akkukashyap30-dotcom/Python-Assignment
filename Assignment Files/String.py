# Different ways of creating a string

s1 = "Hello"
s2 = 'World'
s3 = "Python Programming"
s4 = str("Welcome")

print(s1, s2, s3, s4)

# Concatenating two strings using + operator

a = "Hello"
b = "Python"

result = a + " " + b
print(result)

# Finding the length of the string

text = "Python"
print(len(text))

# Extract a string using substring

text = "Python Programming"
substring = text[0:9]

print(substring)

# Searching in strings using index()

text = "Learn computer"
print(text.index("computer"))

# Matching a string against a Regular Expression

import re

text = "Hello123"
pattern = r"\w+"

if re.fullmatch(pattern, text):
    print("Match found")
else:
    print("No match")

# Comparing strings

a = "apple"
b = "banana"

print(a == b)
print(a != b)

# startsWith(), endsWith() and compareTo()

text = "Python Programming"

print(text.startswith("Python"))
print(text.endswith("Programming"))

# compareTo equivalent
print((text > "Java"))  # True or False

#Trimming strings with strip()

text = "   Hello Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Replacing characters in strings with replace()

text = "Hello World"
print(text.replace("World", "Python"))

# Splitting strings with split()

text = "Python is easy"
words = text.split(" ")

print(words)

# Converting integer objects to strings

num = 100
text = str(num)

print(text)
print(type(text))

# Converting to uppercase and lowercase

text = "Python Programming"

print(text.upper())
print(text.lower())








