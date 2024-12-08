# Task 1: Check if a Year is a Leap Year
import calendar

def is_leap_year(year):
    return calendar.isleap(year)

# Task 2: Display Date and Time Information
import time
from datetime import datetime

def display_datetime_info():
    print("Current Date and Time:", datetime.now())
    print("Current Year:", datetime.now().year)
    print("Month of the Year:", datetime.now().strftime("%B"))
    print("Week Number of the Year:", datetime.now().isocalendar()[1])
    print("Weekday of the Week:", datetime.now().strftime("%A"))
    print("Day of the Year:", datetime.now().timetuple().tm_yday)
    print("Day of the Month:", datetime.now().day)
    print("Day of the Week:", datetime.now().weekday())

# Task 3: Print Yesterday, Today, and Tomorrow
def print_dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
    print("Today:", today.strftime("%Y-%m-%d"))
    print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

# Task 4: Check Palindrome and Find Longest Palindromic Substring
def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(string):
    n = len(string)
    longest = ""
    for i in range(n):
        for j in range(i, n):
            substring = string[i:j+1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

# Task 5: Graphics Package and Subpackage
# graphics/rectangle.py
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

# graphics/circle.py
import math

def circle_area(radius):
    return math.pi * radius**2

def circle_perimeter(radius):
    return 2 * math.pi * radius

# graphics/graphics3D/cuboid.py
def cuboid_area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + length * height)

def cuboid_volume(length, breadth, height):
    return length * breadth * height

# graphics/graphics3D/sphere.py
def sphere_area(radius):
    return 4 * math.pi * radius**2

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3
