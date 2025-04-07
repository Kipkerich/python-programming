n = int(input().strip())
binary = format(n, 'b')
ones = 0
zero = 0

for zero_or_ones in binary:
    if zero_or_ones == '1':
        ones += 1
        if ones > zero:
            zero = ones
    else:
        ones = 0
print(zero)
