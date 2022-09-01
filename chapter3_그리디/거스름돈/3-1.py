n = 1260
count = 0
coinTypes = [500, 100, 50, 10]

for coin in coinTypes:
    count += n // coin
    n %= coin
print (count)