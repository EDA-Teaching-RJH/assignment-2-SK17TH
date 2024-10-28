# Given list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Sort the list in ascending order
numbers.sort()

# Remove all occurrences of the number 1
numbers = [num for num in numbers if num != 1]

# Add the numbers 7 and 8 to the end of the list
numbers.append(7)
numbers.append(8)

# Print the final list
print(numbers)
