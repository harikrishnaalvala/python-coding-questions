def find_pairs_with_sum(arr, target_sum):
    seen = set()
    pairs = []

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Example usage
arr = [1, 2, 3, 4, 5, 6]
target_sum = 7
print("Pairs with sum", target_sum, ":", find_pairs_with_sum(arr, target_sum)) # Pairs with sum 7 : [(4, 3), (5, 2), (6, 1)]
