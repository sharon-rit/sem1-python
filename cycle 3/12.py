def display_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i * j, end=' ')
        print()

steps = int(input("Enter the number of steps for the pyramid: "))
display_pyramid(steps)
