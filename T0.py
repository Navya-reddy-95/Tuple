'''
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
# Input: tuple elements in a single line and the number to count
input_values = input("Enter tuple values separated by space: ")
x = int(input("Enter the number to count: "))

# Convert the input string into a tuple of integers
tuple_values = tuple(map(int, input_values.split()))

# Count occurrences of x in the tuple
count_x = tuple_values.count(x)

# Calculate the factorial of the count
factorial = 1
for i in range(1, count_x + 1):
    factorial *= i

# Output the result
print(factorial)
