# SET A

# 1. Program to sort a list in non-decreasing order without using built-in functions.
def sort_list(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Input list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Sorting the list
sort_list(numbers)

print("Sorted list:", numbers)


# 2. Function to print letters in non-increasing order of frequency of their occurrences.
def list_of_frequency(string):
    frequency = {}
    
    # Count frequency of each character
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Sort the characters by frequency in non-increasing order
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the characters by frequency
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")

# Input string
input_string = input("Enter a string: ")

list_of_frequency(input_string)


# SET B

# 1. Program to determine if the string is a palindrome without using slicing or string functions.
def is_palindrome(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

# Input string
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 2. Program to find the value for Sine(x) up to n terms using the series.
import math

def sine_series(x, n):
    sine_value = 0
    for i in range(n):
        sign = (-1) ** i
        sine_value += sign * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return sine_value

# Input
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

result = sine_series(x, n)
print(f"Sine({x}) up to {n} terms: {result}")


# SET C

# 1. Armstrong number check and generation function.
# Create Armstrong.py file
# Armstrong.py
def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == number

def generate_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end+1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Main program
import Armstrong

start = int(input("Enter start limit: "))
end = int(input("Enter end limit: "))

armstrong_numbers = Armstrong.generate_armstrong_numbers(start, end)
print("Armstrong numbers between", start, "and", end, "are:", armstrong_numbers)


# 2. Function that rotates a list to the right by a given number of steps.
def rotate_list(lst, steps):
    steps = steps % len(lst)  # To handle steps larger than list length
    return lst[-steps:] + lst[:-steps]

# Input list and steps
lst = list(map(int, input("Enter numbers separated by space: ").split()))
steps = int(input("Enter number of steps to rotate: "))

rotated_lst = rotate_list(lst, steps)
print("Rotated list:", rotated_lst)


# SET D

# 1. Program to determine if a year is a leap year using if-else.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Input year
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# 2. Program to maintain student records using a dictionary.
def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_above_average(students, average):
    for student, marks in students.items():
        if calculate_average(marks) > average:
            print(student)

# Student records
students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 95, 91],
    "David": [70, 75, 72]
}

# Input threshold average
threshold = float(input("Enter the threshold average: "))

# Display students with average above the threshold
display_above_average(students, threshold)
