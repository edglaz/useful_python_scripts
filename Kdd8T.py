#!/usr/bin/env python3
import random
import math
import time

class RandomNumberGenerator:
    def __init__(self):
        # Randomly choose which number sequences to generate
        self.sequences = random.sample([
            self.generate_primes,
            self.generate_fibonacci,
            self.generate_perfect_squares,
            self.generate_random_integers,
            self.generate_geometric_sequence
        ], 3)
        
        # Random count between 5 and 15
        self.count = random.randint(5, 15)
    
    def generate_primes(self):
        """Generate prime numbers"""
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        primes = []
        num = 2
        while len(primes) < self.count:
            if is_prime(num):
                primes.append(num)
            num += 1
        
        return f"Prime numbers: {primes}"
    
    def generate_fibonacci(self):
        """Generate Fibonacci sequence"""
        fibonacci = [0, 1]
        while len(fibonacci) < self.count:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
        return f"Fibonacci sequence: {fibonacci}"
    
    def generate_perfect_squares(self):
        """Generate perfect squares"""
        squares = [i * i for i in range(1, self.count + 1)]
        return f"Perfect squares: {squares}"
    
    def generate_random_integers(self):
        """Generate random integers"""
        # Random range between 1-100
        min_val = random.randint(1, 50)
        max_val = min_val + random.randint(50, 200)
        
        numbers = [random.randint(min_val, max_val) for _ in range(self.count)]
        return f"Random integers ({min_val}-{max_val}): {numbers}"
    
    def generate_geometric_sequence(self):
        """Generate geometric sequence"""
        # Random ratio between 2 and 5
        ratio = random.randint(2, 5)
        start = random.randint(1, 10)
        
        sequence = [start * (ratio ** i) for i in range(self.count)]
        return f"Geometric sequence (start={start}, ratio={ratio}): {sequence}"

if __name__ == "__main__":
    # Use current time as seed for more randomness
    random.seed(time.time())
    
    generator = RandomNumberGenerator()
    
    print(f"Generating {generator.count} numbers for each sequence")
    print("-" * 50)
    
    for sequence_generator in generator.sequences:
        print(sequence_generator())
        print()
