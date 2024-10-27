def factors(num):
    result = []
    i = 1
    while i <= num:
        if num % i == 0:
            result.append(i)
        i += 1
    return result

number = int(input("Enter a number to find its factors: "))
print(f"Factors of {number}: {factors(number)}")
