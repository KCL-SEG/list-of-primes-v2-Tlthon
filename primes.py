"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes : int):
    # validity check
    if number_of_primes < 1 :
        raise ValueError("number of primes should be more than or equal to one") 
    list_of_primes = [2]
    number = 3
    while(len(list_of_primes) < number_of_primes) :
        if isPrime(number, list_of_primes) :
            list_of_primes.append(number)   

        number += 1
    return list_of_primes

def isPrime(number : int, prime_list: list) -> bool:
    for prime in prime_list:
        if number % prime == 0:
            return False
        elif prime * prime >= number:
            return True
