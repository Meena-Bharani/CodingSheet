def find_prime_factor(number): # ex: 13
    factors = []
    divisor = 2 # starts with 2
    while divisor <= number: # keep doing from 2 to the number # check if 
        if number % divisor == 0: # if number can be divisible by divisor
            factors.append(divisor) # add with the result
            number = number // divisor # get the reminder after dividing the value
