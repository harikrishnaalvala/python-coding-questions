arr = [1,2,3,4,2]

seen = set()

for i in arr:
    if i in seen:
        print(i)
        break
    seen.add(i)
