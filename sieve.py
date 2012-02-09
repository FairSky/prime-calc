import math

def prime_generator(upper_bound):
    garbage_numbers = set()
    
    curr_num = 1
    
    while curr_num <= upper_bound:
        curr_num = curr_num + 1
        
        while curr_num in garbage_numbers:
            # This is a garbage number, so keep incrementing until it's not.
            curr_num = curr_num + 1
        
        # This is not a garbage number -- therefore it is a prime.
        yield curr_num
        
        garbage_numbers = trash_multiples(curr_num, upper_bound, garbage_numbers)

def trash_multiples(curr_num, upper_bound, garbage_numbers):
    multiplier = curr_num
    
    while curr_num <= upper_bound:
        curr_num = curr_num + multiplier
        garbage_numbers.add(curr_num)
    
    return garbage_numbers

def find_primes_in_range(lower_bound, upper_bound, progress_window = None):
    primes = []
    curr_prime = 0
    generator = prime_generator(upper_bound)
    
    if lower_bound == 1:
        primes.append(1)
    
    while curr_prime <= upper_bound:
        if progress_window.wasCanceled() == True:
            break
        
        try:
            curr_prime = generator.next()
        except StopIteration:
            break
        
        progress_window.setValue(curr_prime)
        primes.append(curr_prime)
    
    if progress_window.value() < upper_bound:
        progress_window.setValue(upper_bound)
    
    return primes

def is_prime(curr_num, progress_window = None):
    if curr_num % 2 == 0:
        return False
    
    primes = find_primes_in_range(curr_num, curr_num, progress_window)
    
    if primes.count(curr_num) > 0:
        return True
    else:
        return False

def build_prime_list(input_number, prime_list):
    for index in xrange(0, len(prime_list)):
        if input_number % prime_list[index] == 0:
            return False
    
        if prime_list[index] > math.sqrt(input_number * 1.0):
            prime_list.append(input_number)
            return True

def find_x_primes(lower_bound, quantity, progress_window = None):
    prime_list = []
    prime_list.append(2)
    curr_num = 3    
    return_list = []
    
    if lower_bound <= 2:
        return_list.append(1)
        
        if lower_bound == 2:
            return_list.append(2)
    
    while len(return_list) < quantity:
        if progress_window.wasCanceled() == True:
            break
        
        if build_prime_list(curr_num, prime_list) == True:                
            prime_list.append(curr_num)
            
            if curr_num >= lower_bound:
                progress_window.setValue(progress_window.value() + 1)
                return_list.append(curr_num)
        
        curr_num = curr_num + 2
    
    progress_window.setValue(quantity)
    
    return return_list
    