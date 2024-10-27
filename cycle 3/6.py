def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def alternate_primes(n):
    count = 0
    for num in range(2, n + 1):
        if is_prime(num):
            count += 1
            if count % 2 == 0:  # Print alternate primes
                print(num)

limit = int(input("Enter the upper limit: "))
print("Alternate prime numbers up to N:")
alternate_primes(limit)
