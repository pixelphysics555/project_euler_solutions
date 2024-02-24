# Sum of Primes < 2_000_000
import time
import threading
from numpy import sqrt

def is_prime_odd(num):
    """Checks if a given number greater than 2 is prime."""

    for i in range(3, round(sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True

def test():
    print(f'Check for 9: {is_prime_odd(9)}.')
    print(f'Check for 37: {is_prime_odd(37)}.')

# test()

def thread_check(idx):
    """Separates the list of odd numbers into threads 
    of length 10_000;
    runs through each thread;
    checks whether each number is prime;
    adds the primes to a list; 
    sorts the complete list;
    and prints the time it takes to perform, 
    length of primes list, 
    and sum of the primes."""

    time.sleep(1)
    primes = []
    start_idx = idx * 10_000
    end_idx = start_idx + 10_000
    for i in two_mil_odd[start_idx:end_idx]:
        if is_prime_odd(i) == True:
            primes.append(i)
    big_primes.extend(primes)
    
    if idx % 10 == 0:
        print('Thread added: ' + str(idx))

    if idx == rng - 1:
        time.sleep(1)

        big_primes.insert(0, 2)
        big_primes.sort()
        
        end = time.time()
        print(f'Took {round(end - start, 3)} seconds.')
        print('Number of primes: ' + str(len(big_primes)))
        print('Sums of primes: ' + str(sum(big_primes)))

start = time.time()

two_mil_odd = [i for i in range(3, 2_000_000, 2)]

big_primes = []

rng = int(1_000_000 / 10_000)
for i in range(rng):
    thread_obj = threading.Thread(target=thread_check, \
            args=[i])
    thread_obj.start()
