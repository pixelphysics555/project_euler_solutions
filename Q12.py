#!/usr/bin/env python3 # Find the first triangular number with 500 divisors import logging
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Start of program.")

def triangular_number(n):	
    """Returns the nth triangular number."""

    return int((n * (n + 1)) / 2)

def number_of_divisors(num):	
    """Returns the number of divisors of a number."""

    logging.debug(f"Start of number_of_divisors({num}).")
    sqrt = num ** 0.5
    total_divs = 0
    
    for i in range(1, int(sqrt) + 1):
        if num / i == i:
            total_divs += 1
            logging.debug(f"Divisible by {i}.")
        elif num % i == 0:
            logging.debug(f"Divisible by {i} and {int(num / i)}.")
            total_divs += 2

    logging.debug(f"Total divisors = {total_divs}.")
    return total_divs

if __name__ == "__main__":
    NUMBER_OF_DIVISORS_TO_BEAT = 500
    i = 1
    while number_of_divisors(triangular_number(i)) < NUMBER_OF_DIVISORS_TO_BEAT:
        if i % 100 == 0:
            logging.info(f"i = {i}.")
        i += 1
    print(triangular_number(i))
    print(number_of_divisors(triangular_number(i)))
    logging.info("End of program.")
