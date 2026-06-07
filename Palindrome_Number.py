num = 121

if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# another method Without converting to string

n = 121
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(temp == rev)

