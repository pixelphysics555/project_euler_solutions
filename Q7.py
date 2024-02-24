def is_a_prime(value):
    for i in range(value):
        if i == 0 or i == 1:
            i += 1
        elif value % i == 0:
            return False
    return True


i = 2
listOfPrimes = []
while len(listOfPrimes) <= 10000:
    if is_a_prime(i) == True:
        listOfPrimes.append(i)
        i += 1
    else:
        i += 1

print(listOfPrimes[-1])
