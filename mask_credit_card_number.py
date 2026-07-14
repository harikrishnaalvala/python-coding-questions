def mask_credit_card_number(card_number):
    # Check if the size of the credit card number is even and >= 6
    if len(card_number) >= 6 and len(card_number) % 2 == 0:
        # Calculate the start and end index of the middle 4 digits
        start_index = (len(card_number) - 4) // 2
        end_index = start_index + 4

        # Mask the credit card number
        masked_number = card_number[:start_index] + "X" * (end_index - start_index) + card_number[end_index:]

        return masked_number
    else:
        return "Invalid credit card number"

# Example usage
credit_card_number = "1234567890123456"
print(mask_credit_card_number(credit_card_number))  # Output: "1234XXXXXXXX3456"
