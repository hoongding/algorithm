n = int(input())
digit_sum = 0
inspect = 0
for i in range(n+1):
    digit = list(map(int, str(i)))
    digit_sum = sum(digit)
    inspect = i + digit_sum    
    if n == inspect:
        print(i)
        break
    if n == i:
        print(0)