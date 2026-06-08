arr = [1,2,3]

for i in range(len(arr)):
    total = 0
    for j in range(i, len(arr)):
        total += arr[j]
        print(total)
