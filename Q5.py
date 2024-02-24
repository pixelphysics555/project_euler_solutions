import numpy as np

#stands for 'Divisible by everything under 20':
def dbeu20(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True

#Main loop
x = np.math.factorial(20)
for i in range(2520, x, 20):
    if dbeu20(i) == True:
        print(i)
        break
