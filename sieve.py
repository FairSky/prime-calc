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

def find_primes_in_range(lower_bound, upper_bound, progress_window):
    primes = []
    generator = prime_generator(upper_bound)
    
    if lower_bound == 1:
        primes.append(1)
    
    while True:
        if progress_window.wasCanceled():
            return
        
        try:
            curr_prime = generator.next()
        except StopIteration:
            break
        
        if curr_prime <= upper_bound:
            progress_window.setValue(curr_prime)
            primes.append(curr_prime)
    
    return primes

def is_prime(curr_num, progress_window):
    if curr_num % 2 == 0:
        return False
    
    primes = find_primes_in_range(curr_num, curr_num, progress_window)
    
    if primes.count(curr_num) > 0:
        return True
    else:
        return False
    