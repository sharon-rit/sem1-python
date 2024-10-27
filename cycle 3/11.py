def is_armstrong(num):
    sum_of_cubes = 0
    original_num = num
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    return sum_of_cubes == original_num

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
