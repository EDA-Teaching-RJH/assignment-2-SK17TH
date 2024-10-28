
import random

# Create a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Original list:", random_numbers)

# Use a while loop to remove all even numbers from the list
index = 0
while index < len(random_numbers):
    if random_numbers[index] % 2 == 0:  # Check if the number is even
        random_numbers.pop(index)  # Remove the even number
    else:
        index += 1  # Move to the next index only if the current number is odd

# Print the remaining odd numbers
print("Remaining odd numbers:", random_numbers)
