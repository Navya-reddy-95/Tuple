'''
 Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
# Input the number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Input the tuple elements
print("Enter the elements (one per line):")
for _ in range(n):
    elements.append(int(input()))

# Convert the list to a tuple
elements_tuple = tuple(elements)

# Find the maximum value using the predefined max() method
max_value = max(elements_tuple)

# Output the result
print(max_value)
