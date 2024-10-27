def sum_divisible_by_6_not_4(limit):
    total = 0
    for i in range(limit):
        if i % 6 == 0 and i % 4 != 0:
            total += i
    return total

upper_limit = int(input("Enter the upper limit: "))
print(f"Sum of integers divisible by 6 but not by 4 below {upper_limit}: {sum_divisible_by_6_not_4(upper_limit)}")
