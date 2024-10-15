'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
# Input: tuple elements in a single line
input_values = input("Enter tuple elements separated by space: ")

# Convert the input string into a tuple of integers
tuple_values = tuple(map(int, input_values.split()))

# Initialize a variable to hold the sum
total_sum = 0

# Iterate through the tuple and calculate the sum
for value in tuple_values:
    total_sum += value

# Output the result
print(total_sum)
