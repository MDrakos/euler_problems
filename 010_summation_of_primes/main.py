def primes(n):
    """Given the number of the prime this function will return a list of primes
    This is my initial attempt and is much slower than the sieve of eratosthenes
    which is implemented below.

    :param n: integer
    :return: list
    """
    # initial prime value
    primes_list = [2]

    # initial attempt to find primes
    attempt = 3

    # iterates up while the attempt value is less then n
    # if there is a remainder from the attempt/prime for all current primes then we have not found a prime,
    # we iterate attempt and try again. Otherwise we have found a prime and append to the list
    # Finally we return the list of primes
    while attempt < n:
        if all(attempt % prime != 0 for prime in primes_list):
            primes_list.append(attempt)
        attempt += 2
    return primes_list


def eratosthenes2(n):
    """Sieve or Eratosthenes implementation using set lookup.
    Set objects are usually faster (O(log n)) than lists since set.update method
    avoids explicit iteration in the interpreter

    :param n: integer
    """
    # Again, using a set since set.update is faster
    multiples = set()

    # Set the range to find primes
    # Use xrange since this was compiled in Python2 and xrange is the closest to Python3's implementation of range
    for i in xrange(2, n + 1):

        # if i is not in multiples we have a prim
        if i not in multiples:
            # return the generator
            yield i

            # update the multiples set with all values from i*i to our max in steps of i
            multiples.update(xrange(i * i, n + 1, i))


# print sum(primes(200000))

print(sum(list(eratosthenes2(2000000))))
