num = int(input('Enter any number:'))
greatest = 0
res = num

while res > 0:
    n = res % 10
    if n > greatest:
        greatest = n
        if greatest == 9:
            break
    if n < greatest:
        break
    res = res // 10
print(f'The greatest is {greatest}')
