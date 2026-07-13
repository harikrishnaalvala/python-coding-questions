def print_pattern(rows):
    num = 1

    # Increasing rows
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()  # Newline after each row

    # Decreasing rows
    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()  # Newline after each row

# Example usage
print_pattern(4)  # Middle row is the 4th row
