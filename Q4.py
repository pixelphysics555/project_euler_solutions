# Largest palindromic product of 3 digit numbers
#Max: 998001
#Min: 10000
def is_a_prime(value):
    for i in range(value):
        if i == 0 or i == 1:
            i += 1
        elif value % i == 0:
            return False
    return True

#Determines if the entered number is in fact a palindrome
def palindrome(number):
    number = str(number)
    listOfDigits = list(number)
    antiList = listOfDigits[::-1]
    if listOfDigits == antiList:
        return True
    else:
        return False

#Stands for 'Product of two 3-digit numbers' and checks if that is true
def pottdn(number):
    if is_a_prime(number) == True:
        return False
    elif is_a_prime(number) == False:
        i = 100
        while i < 1000:
            if number % i != 0:
                i += 1
                continue
            elif number % i == 0:
                factor = number / i
                if len(str(int(factor))) == 3 and len(str(int(i))) == 3:
                    return True
                    break
                else:
                    i += 1
                    continue
        if i == 1000:
            return False


#Main loop
i = 997800
while i > 10001:
    i -= 1
    if palindrome(i) == True:
        if pottdn(i) == True:
            print(i)
            break
