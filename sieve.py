import math
from PySide.QtCore import *
from PySide.QtGui import *

# Prime Number Sieve using a loop by Scott Rothrock

__prime_master_list__ = []

def is_prime(input_number):
    for index in xrange(0, len(__prime_master_list__)):
        if input_number % __prime_master_list__[index] == 0:
            return False
    
        if __prime_master_list__[index] > math.sqrt(input_number * 1.0):
            __prime_master_list__.append(input_number)
            return True

def find_primes_in_range(lower_bound, upper_bound, primes_found, progress_bar = None):
    for input_number in xrange(lower_bound, upper_bound + 1, 2):  
        if is_prime(input_number) and lower_bound <= input_number <= upper_bound:                
            primes_found.append(input_number)
            
            if progress_bar != None:
                progress_bar.setValue(input_number)
    
    return primes_found

def search_range(lower_bound, upper_bound, progress_bar = None, thread_storage = None):
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
    
    #if thread_storage != None:
        #thread_storage.put_nowait(find_primes_in_range(lower_bound, upper_bound, primes_found, progress_bar))
    #else:
    return find_primes_in_range(lower_bound, upper_bound, primes_found, progress_bar)

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