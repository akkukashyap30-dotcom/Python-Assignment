# Function to add integer values of an array

def array_sum(arr):
    return sum(arr)

print(array_sum([1, 2, 3, 4]))

# Function to calculate average of array

def array_average(arr):
    return sum(arr) / len(arr)

print(array_average([10, 20, 30]))

# Program to find index of an array element

arr = [10, 20, 30, 40]
element=35

if element in arr:
    print(arr.index(element))
else:
    print("Element not found")

# Function to test if array contains a specific value

def contains_value(arr, value):
    return value in arr

print(contains_value([1, 2, 3], 2))

# Function to remove a specific element

def remove_element(arr, value):
    return [x for x in arr if x != value]

print(remove_element([1, 2, 3, 2], 2))

# Function to copy an array

def copy_array(arr):
    return arr.copy()

print(copy_array([1, 2, 3]))

# Function to insert element at a specific position

def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

print(insert_element([1, 2, 4], 2, 3))

# Function to find minimum and maximum value

def min_max(arr):
    return min(arr), max(arr)

print(min_max([10, 5, 20, 3]))

# Function to reverse an array

def reverse_array(arr):
    return arr[::-1]

print(reverse_array([1, 2, 3, 4]))

# Function to find duplicate values

def find_duplicates(arr):
    duplicates = set()
    for x in arr:
        if arr.count(x) > 1:
            duplicates.add(x)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 1]))

# Program to find common values between two arrays

def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(common_elements([1, 2, 3], [2, 3, 4]))

# Method to remove duplicate elements

def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates([1, 2, 2, 3, 3]))

# Method to find second largest number

def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 4, 45, 99]))

# Method to find second largest number (same logic)

def second_largest(arr):
    arr = list(set(arr))
    arr.sort(reverse=True)
    return arr[1]

print(second_largest([5, 10, 15, 20]))

# Method to count even and odd numbers

def count_even_odd(arr):
    even = odd = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5]))


# Function to get difference of largest and smallest value

def difference_max_min(arr):
    return max(arr) - min(arr)

print(difference_max_min([10, 2, 8, 20]))

# Method to verify array contains two specified elements (12, 23)

def contains_elements(arr):
    return 12 in arr and 23 in arr

print(contains_elements([5, 12, 23, 9]))

# Program to remove duplicates and return new array

def unique_array(arr):
    new_arr = []
    for x in arr:
        if x not in new_arr:
            new_arr.append(x)
    return new_arr

print(unique_array([1, 2, 2, 3, 4, 4]))



