# Experiment - 1
# Aim: Write a program to print the Fibonacci series using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")

# Experiment - 2
# Aim: Write a menu-driven calculator using separate functions for different operations.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid input.")

# Experiment - 3
# Aim: Write a program to print the nth prime number using a function to check if a number is prime.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    number = 2
    while True:
        if is_prime(number):
            count += 1
            if count == n:
                return number
        number += 1

n = int(input("Enter the value of n: "))
print(f"The {n}th prime number is {nth_prime(n)}")

# Experiment - 4
# Aim: Write lambda functions to find the area of a square, rectangle, and triangle.

area_square = lambda side: side ** 2
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height

print("Area of square:", area_square(5))
print("Area of rectangle:", area_rectangle(5, 10))
print("Area of triangle:", area_triangle(10, 5))

# Experiment - 5
# Aim: Write a program to display powers of 2 using an anonymous function with map.

n = int(input("Enter the number of terms: "))
powers_of_2 = list(map(lambda x: 2 ** x, range(n)))
print("Powers of 2:", powers_of_2)

# Experiment - 6
# Aim: Write a program to sum the series 1/1! + 4/2! + 27/3! + ..... + nth term.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_series(n):
    return sum([(i ** i) / factorial(i) for i in range(1, n + 1)])

n = int(input("Enter the number of terms: "))
print("Sum of the series:", sum_series(n))

# Experiment - 7
# Aim: Write a function called compare to compare the first n characters of two strings.

def compare(S1, S2, n):
    return S1[:n] == S2[:n]

S1 = input("Enter first string: ")
S2 = input("Enter second string: ")
n = int(input("Enter the number of characters to compare: "))
print("Result:", compare(S1, S2, n))

# Experiment - 8
# Aim: Write a program using functions to implement formulas for permutations and combinations.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"P({n}, {r}) = {permutation(n, r)}")
print(f"C({n}, {r}) = {combination(n, r)}")
