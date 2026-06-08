arr = [1,4,20,3,10,5]
target = 33

start = 0
curr = 0

for end in range(len(arr)):
    curr += arr[end]

    while curr > target:
        curr -= arr[start]
        start += 1

    if curr == target:
        print(start, end)
        break
