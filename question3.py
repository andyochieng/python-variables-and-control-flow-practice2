def sum_of_numbers(nums):
    total = 0
    for num in nums:  # Using a for loop to iterate through each number in the list
        total += num
    return total

# Example usage
nums = [1, 2, 3, 4, 5]
print("The sum is:", sum_of_numbers(nums))
