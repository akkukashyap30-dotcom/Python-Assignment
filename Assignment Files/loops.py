# Print “Bright IT Career” ten times using for loop
for a in range(5):
    print("Bright IT Career")

#  Print 1 to 20 numbers using while loop
    k = 1
while k <= 10:
    print(k)
    k += 1

# Program for equal (==) and not equal (!=) operators

a = 10
b = 20

print(a == b)
print(a != b) 

# Print odd and even numbers

for a in range(1, 11):
    if a % 2 == 0:
        print(a, "is Even")
    else:
        print(a, "is Odd")

# Print largest number among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Print even numbers between 10 and 20 using while

i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Print 1 to 10 using do-while loop    

i = 1
while True:
    print(i)
    i += 1
    if i > 15:
        break

# Check Armstrong number

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Check Prime number

num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")   

# Check Palindrome number 

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

 # Check EVEN or ODD using switch

    num = int(input("Enter a number: "))

switch = { 0: "Even", 1: "Odd"}

print(switch[num % 2])

# Print Gender using switch (M/F)

gender = input("Enter gender (M/F): ").upper()

switch = { "M": "Male", "F": "Female"}

print(switch.get(gender, "Invalid Input"))

