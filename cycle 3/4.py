def even_perfect_squares(start, end):
    results = []
    for num in range(start, end + 1):
        # filtering out only the 4 digit even numbers
        if 1000 <= num <= 9999 and num % 2 == 0:
            # taking the root of every 4 digit even number between the range
            root = int(num**0.5)
            # Check if it's a perfect square
            if root * root == num:  
                digits = str(num)
                if all(int(digit) % 2 == 0 for digit in digits):
                    results.append(num)
                
    return results

start_range = int(input("Enter start range: "))
end_range = int(input("Enter end range: "))
print(f"Four-digit even perfect squares: {even_perfect_squares(start_range, end_range)}")
