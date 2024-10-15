'''
 Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
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

# Find the minimum value using the predefined min() method
min_value = min(elements_tuple)

# Output the result
print(min_value)
