'''
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
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

# Calculate the sum using the predefined sum() method
total_sum = sum(elements_tuple)

# Output the result
print(total_sum)
