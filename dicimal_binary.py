def decimal_binary(num):
    if num >= 1:
        decimal_binary(num // 2)
    print(num%2,end='')


decimal_binary(24)
