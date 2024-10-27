def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

numbers = [1, 2, 3, 4, 5]  # Example list
print("list = ",numbers)
print(f"Sum of the list is: {sum_of_list(numbers)}")
