# Problem 4

# Write a Python function that creates and returns a list of prime numbers
# between 2 and N, inclusive, sorted in increasing order. A prime number is
# a number that is divisible only by 1 and itself. This function takes in
# an integer and returns a list of integers.


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False

    upper_lim = int(n ** 0.5)

    for k in range(3, upper_lim + 1, 2):
        if n % k == 0:
            return False

    return True


def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    primes_list = []
    for n in range(2, N + 1):
        if is_prime(n):
            primes_list.append(n)

    return primes_list


def main():
	print(primes_list(47))


if __name__ == '__main__':
    main()
