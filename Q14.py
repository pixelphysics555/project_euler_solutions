#!/usr/bin/env python3

# Which starting number, under one million, produces the longest Collatz sequence?
import copy
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Start of program.")


#TODO:
""" 
1. Write function for running through Collatz sequence.
2. At each step, check if number has already been evaluated.
3. Add steps up to this point to previous evaluation.
4. Keep track of longest chain and return longest after evaluating up to 1,000,000.
"""

def collatz(num):	
    """Returns the next term in the Collatz sequence for a number."""

    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1

def main():	
    """Main program"""
    
    chain_lens = {}

    for i in range(2, 1_000_000):
        counter = 1
        num = copy.copy(i)
        while num != 1:
            num = collatz(num)
            if num in chain_lens.keys():
                # Add key to counter and append to dictionary
                counter += chain_lens[num]
                # logging.debug(f"{num} was found in the sequence for {i}.")
                break
            else:
                counter += 1

        chain_lens.setdefault(i, counter)

        if i % 1_000 == 0:
            logging.debug(f"i = {i}.")
            logging.debug(f"Chain length for {i} is {counter}.")

    longest_chain_len = max(chain_lens.values())
    logging.info(f"Longest chain length = {longest_chain_len}.")
    number_with_longest_chain = list(chain_lens.values()).index(longest_chain_len)

    return number_with_longest_chain
   

if __name__ == "__main__":
    print(main())
    logging.info("End of program.")
