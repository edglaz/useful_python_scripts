def generate_permutations(elements):
    # Base case: if the list has only one element, return it as a single permutation
    if len(elements) <= 1:
        return [elements]
    
    # List to store all permutations
    result = []
    
    # Try each element as the first element
    for i in range(len(elements)):
        # Current element to place at the beginning
        current = elements[i]
        
        # Remaining elements (excluding the current one)
        remaining_elements = elements[:i] + elements[i+1:]
        
        # Generate permutations of the remaining elements
        remaining_permutations = generate_permutations(remaining_elements)
        
        # Add current element to the beginning of each permutation of the remaining elements
        for p in remaining_permutations:
            result.append([current] + p)
    
    return result

# Function to display examples nicely
def print_example(elements):
    print(f"List: {elements}")
    permutations = generate_permutations(elements)
    print(f"Permutations ({len(permutations)}):")
    for p in permutations:
        print(f"  {p}")
    print()

# Example 1: A list with 3 numbers
print_example([1, 2, 3])

# Example 2: A list with characters
print_example(['a', 'b', 'c'])

# Example 3: A list with 2 elements
print_example([10, 20])

# Example 4: An empty list
print_example([])

# Example 5: A list with 1 element
print_example([5])
