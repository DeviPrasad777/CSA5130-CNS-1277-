import math

def factorial(n):
    return math.factorial(n)

def calculate_possible_keys():
    total_possible_keys = factorial(25)
    print("Approximate number of possible keys without considering identical encryption results:", total_possible_keys)

    # Calculate the number of effectively unique keys
    # Here we'll consider 'IJ' and 'JI' as interchangeable
    identical_permutations = factorial(2)  # 'IJ' and 'JI'
    total_effective_keys = total_possible_keys / identical_permutations
    print("Approximate number of effectively unique keys, considering identical encryption results:", total_effective_keys)

calculate_possible_keys()
