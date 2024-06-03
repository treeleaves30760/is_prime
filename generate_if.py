import argparse

class PrimeGenerator:
    def __init__(self, args):
        self.n = args.n
        self.output_file = args.o
        self.lang = args.l
        self.n_len = len(str(self.n))
        
    def sieve_of_eratosthenes(self):
        primes = [True] * (self.n + 1)
        primes[0] = primes[1] = False

        p = 2
        while p * p <= self.n:
            if primes[p]:
                for i in range(p * p, self.n + 1, p):
                    primes[i] = False
            p += 1

        return primes

    def generate_is_prime(self):
        primes = self.sieve_of_eratosthenes()
        
        file_name = self.output_file
        if self.lang == 'cpp':
            file_name += '.hpp'
        elif self.lang == 'py':
            file_name += '.py'
            
        with open(file_name, 'w') as f:
            if self.lang == 'cpp':
                f.write('#include <vector>\n\n')
                f.write('bool is_prime(int n) {\n')
                f.write('\tif (n == 0 || n == 1) return false;\n')
                for ind, i in enumerate(primes):
                    if i:
                        f.write(f'\telse if (n == {ind: >{self.n_len}}) return  true;\n')
                    else:
                        f.write(f'\telse if (n == {ind: >{self.n_len}}) return false;\n')
                f.write('}\n')
            elif self.lang == 'py':
                f.write('def is_prime(n):\n')
                for ind, i in enumerate(primes):
                    if ind == 0:
                        f.write(f'\tif n == {ind: >{self.n_len}}:\n\t\treturn False\n')
                    elif i:
                        f.write(f'\telif n == {ind: >{self.n_len}}:\n\t\treturn  True\n')
                    else:
                        f.write(f'\telif n == {ind: >{self.n_len}}:\n\t\treturn False\n')

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, default=100000, help='Value of N')
parser.add_argument('-o', type=str, default='is_prime', help='Output file')
parser.add_argument('-l', type=str, default='py', help='''support: py, cpp''')
args = parser.parse_args()

prime_generator = PrimeGenerator(args)
prime_generator.generate_is_prime()