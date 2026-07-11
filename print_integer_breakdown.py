def print_integer_breakdown(number):
    num_str = str(number)
    length = len(num_str)
    parts = []

    for i, digit in enumerate(num_str):
        if digit != "0":
            part = digit + "0" * (length - i - 1)
            parts.append(part)

    breakdown = " + ".join(parts)
    print(breakdown)

# Example usage
print_integer_breakdown(43018) # 40000 + 3000 + 10 + 8
