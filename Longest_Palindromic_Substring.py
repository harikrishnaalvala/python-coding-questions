s = "babad"

longest = ""

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]

        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub

print(longest)
