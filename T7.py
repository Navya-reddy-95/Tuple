'''
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
# Input: tuple values in a single line and the value to count
input_values = input("Enter tuple values separated by space: ")
x = int(input("Enter the value to count: "))

# Convert the input string into a tuple of integers
tuple_values = tuple(map(int, input_values.split()))

# Count occurrences of x in the tuple
count_x = tuple_values.count(x)

# Output the result
print(count_x)
