import sys
import time
import os
import math

DEBUG = True

def is_prime(n=0, debug=DEBUG):
    if n <= 1:
        if debug:
            print('debug: ' + str(n) + ' is NOT prime')
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if debug:
                print("debug: " + str(n) + " is NOT prime")
            return False
    if debug:
        print('debug: ' + str(n) + ' is prime')
    return True

def get_primes(numbers, debug=DEBUG):
    primes = []
    for i in numbers:
        if is_prime(i, debug):
            primes.append(i)
    if debug:
        print("debug: primes = " + str(primes))
    return primes


if __name__ == '__main__':
    test_vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    primes = get_primes(test_vector, True)
    print('primes: ' + str(primes))

