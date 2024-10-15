'''
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
# Input the tuple elements in a single line
elements = tuple(map(int, input("Enter the tuple elements separated by space: ").split()))

# Get the number of elements in the tuple
num_elements = len(elements)

# Output the result
print(num_elements)
