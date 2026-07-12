def min_coins_for_amount(amount):
    num_five_rupee_coins = amount // 5
    remainder_after_fives = amount % 5

    # Check if the remainder can be paid using 2 rupee coins
    if remainder_after_fives % 2 == 0:
        num_two_rupee_coins = remainder_after_fives // 2
        total_coins = num_five_rupee_coins + num_two_rupee_coins
        return f"5 rupee coins: {num_five_rupee_coins}, 2 rupee coins: {num_two_rupee_coins}, Total coins: {total_coins}"
    else:
        return "It is not possible"

# Example usage
print(min_coins_for_amount(345))
