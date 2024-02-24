# This program will produce the largest prime factor of any number.
# Enter the number you want the factor of in for x.

# Determines whether of not a given number is a prime number:
def is_a_prime(value):
    for i in range(value):
        if i == 0 or i == 1:
            i += 1
        elif value % i == 0:
            return False
    return True

#is_a_prime = lambda x :
# Finds first prime divisor of a given number:
def get_first_prime_factor(number):

    if is_a_prime(number) == True:
        print(str(number))

    else:
        i = 2
        while i < int(number):
            if is_a_prime(i) == True:
                if number % i != 0:
                    i += 1
                    continue
                elif number % i == 0:
                    break
            elif is_a_prime(i) == False:
                i += 1
                continue
        return i

print('Enter the number of which you want the largest prime factor of.')
x = int(input())

# Continuously divides a number by its smallest prime factor until
# the number is no longer composite:
while True:
    factor = get_first_prime_factor(x)
    x = int(x / factor)
    if is_a_prime(x) == True:
        print(x)
        break
    elif is_a_prime(x) == False:
        continue
