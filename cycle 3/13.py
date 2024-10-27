def print_pattern():
    # Upper part of the pattern
    for i in range(1, 6):
        print('* ' * i)
    
    # Lower part of the pattern
    for i in range(4, 0, -1):
        print('* ' * i)

print_pattern()
