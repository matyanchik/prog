result = 4**511 + 2**511 - 511

count_of_ones = bin(result).count('1')

print(count_of_ones)