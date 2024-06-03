import argparse

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return primes

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, help='Value of N')
args = parser.parse_args()

N = args.n if args.n else 10000000
primes = sieve_of_eratosthenes(N)

print(f'def is_prime(n):')
for ind, i in enumerate(primes):
    if ind == 0:
        print(f'\tif n == {ind}:\n\t\treturn False')
    elif i:
        print(f'\telif n == {ind}:\n\t\treturn True')
    else:
        print(f'\telif n == {ind}:\n\t\treturn False')