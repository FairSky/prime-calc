import math
import sys

# Double Python's recursion limit.
sys.setrecursionlimit(3000)

# Prime Number Sieve using recursion by Scott Rothrock

__prime_master_list__ = []

def is_prime(curr_num, primeListPos = 0):
    if curr_num % __prime_master_list__[primeListPos] == 0:
        return None
    
    # Todo: Save __prime_master_list__ to a file.
    if __prime_master_list__[primeListPos] > math.sqrt(curr_num * 1.0):
        __prime_master_list__.append(curr_num)
        return curr_num

    return is_prime(curr_num, primeListPos + 1)

def find_primes_in_range(lower_bound, upper_bound, primes_found = [], curr_num=3):
    # Store the prime so we don't have to recurse several times.
    temp_num = is_prime(curr_num)
    
    if lower_bound <= temp_num <= upper_bound:
        primes_found.append(temp_num)
    
    if curr_num >= upper_bound:
        return primes_found
    else:
        return find_primes_in_range(lower_bound, upper_bound, primes_found, curr_num + 2)

def search_range(lower_bound, upper_bound):
    """
    search_range(lower_bound, upper_bound) finds primes in the range lower_bound to upper_bound and then returns a list.
    Both inputs must be positive integers.
    """
    
    primes_found = []
    
    if len(__prime_master_list__) == 0:
        __prime_master_list__.append(2)
    
    # 1 and 2 are special cases.
    # We know that they are basic primes.
    if lower_bound <= 2:
        if lower_bound == 1:
            primes_found.append(1)
            
        primes_found.append(2)
        lower_bound = 3
    
    return find_primes_in_range(lower_bound, upper_bound, primes_found)

# This isn't the fastest way, but it is the simplest for our purposes.
def find_single(input_number):
    """
    find_single(input_number) returns True if input_number is a prime.
    input_number must be a positive integer.
    """
    
    if __prime_master_list__.count(input_number) > 0:
        return True
    
    if len(search_range(input_number, input_number)) == 0:
        return False
    else:
        return True