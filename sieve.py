import time

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

def find_primes_in_range(lower_bound, upper_bound, window):
    primes = "[]"
    old_time = 0
    generator = prime_generator(upper_bound)
    
    if lower_bound == 1:
        primes = "1 "
    
    while True:
        try:
            curr_prime = generator.next()
        except StopIteration:
            break
        
        curr_time = time.time()
        
        if curr_time - old_time > .09:
            window.progress_bar.setValue(curr_prime)
            old_time = curr_time
        
        if curr_prime <= upper_bound:
            primes = primes + str(curr_prime) + " "
    
    time.sleep(.08)
    
    # Set the progress bar to 100% in case the upper bound was not prime.
    window.progress_bar.setValue(upper_bound)
    
    time.sleep(.08)
    
    window.text_area.insertPlainText(primes)
    
    