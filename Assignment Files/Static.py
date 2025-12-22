# Define a static variable and access it through a class

class Student:
    college = "Apna College"

print(Student.college)

# Define a static variable and access it through an instance

class Student:
    college = "American india foundation" 

s1 = Student()

print(s1.college)

# Define a static variable and change it within the instance

class Student:
    college = "Delhi University"

s1 = Student()

s1.college = "Delhi University"

print(s1.college) 
print(Student.college)

#Define a static variable and change it within the class

class Student:
    college = "ABC College"   # static variable

# Change using class name
Student.college = "XYZ College"

s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college) 


