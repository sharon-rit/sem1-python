def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_digits_in_range(upper_limit):
    for num in range(1, upper_limit + 1):
        digit_sum = sum_of_digits(num)
        if is_prime(digit_sum):
            #print(f"Sum of digits of {num} is {digit_sum}, which is prime.")
            print(f'Sum of digit {num} = {digit_sum}')

limit = int(input("Enter an upper limit: "))
sum_digits_in_range(limit)
