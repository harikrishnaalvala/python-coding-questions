def pay_amount(amount):
    # Calculate the maximum number of Rs.5 coins
    num_rs_5_coins = amount // 5

    # Calculate the remaining amount
    remaining_amount = amount - (num_rs_5_coins * 5)

    # Calculate the number of Rs.2 coins
    num_rs_2_coins = remaining_amount // 2

    # Calculate the total number of coins used
    total_coins = num_rs_5_coins + num_rs_2_coins

    # Return the results
    return f"{num_rs_5_coins}*Rs.5 + {num_rs_2_coins}*Rs.2 = {total_coins}"

# Example usage
inputs = [30, 37, 41]
for amount in inputs:
    print(f"Input: {amount}, Output: {pay_amount(amount)}")
