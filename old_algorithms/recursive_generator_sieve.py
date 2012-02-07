# Hits the recursion limit.

def x_primes(x, prime_list):
    for i in xrange(x):
        yield prime_list.next()

def initial_range(lower_bound):
    while True:
        yield lower_bound
        lower_bound = lower_bound + 1

def primes_in_range(lower_bound, upper_bound, prime_list):
    while True:
        curr_prime = prime_list.next()
        
        if curr_prime > upper_bound:
            return
        else:
            yield curr_prime

def sieve(int_range, curr_num):
    for i in int_range:
        if i % curr_num != 0:
            yield i

def make_prime_list(int_range):
    while True:
        prime = int_range.next()
        yield prime
        int_range = sieve(int_range, prime)

def find_x_primes(x, lower_bound = 2):
    prime_list = []
    
    if lower_bound == 1:
        prime_list.append(1)
        lower_bound = 2
    
    for i in x_primes(x, make_prime_list(initial_range(lower_bound))):
        prime_list.append(i)
    
    return prime_list

def find_primes_in_range(lower_bound, upper_bound, progress_bar = None):
    prime_list = []
    
    if lower_bound == 1:
        prime_list.append(1)
        lower_bound = 2
    
    for i in primes_in_range(lower_bound, upper_bound, make_prime_list(initial_range(lower_bound))):
        prime_list.append(i)
        
        if progress_bar != None:
            progress_bar.setValue(i)
    
    return prime_list
