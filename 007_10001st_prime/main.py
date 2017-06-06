def primes(n):
    """Given the number of the prime this function will return a prime
    """
    # initial prime value
    primes = [2]

    # initial attempt to find primes
    attempt = 3

    # iterates up to given range
    # if there is a remainder from the attempt/prime for all current primes then we have not found a prime,
    # we iterate attempt and try again. Otherwise we have found a prime and append to the list
    # Finally we return the last value in the list
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]


print primes(10001)
