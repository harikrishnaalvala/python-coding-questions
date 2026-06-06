def permutations(s, ans=""):
    if len(s) == 0:
        print(ans)
        return

    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        permutations(left + right, ans + ch)

permutations("ABC") 
