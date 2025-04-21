def generate_subsets(nums, index=0, current=None):
    if current is None:
        current = []
    
    # Base case: if we've processed all elements
    if index == len(nums):
        return [current]
    
    # Recursive case:
    # 1. Include the current element
    include = generate_subsets(nums, index + 1, current + [nums[index]])
    
    # 2. Exclude the current element
    exclude = generate_subsets(nums, index + 1, current)
    
    # Combine results
    return include + exclude

# Example usage
def print_example(nums):
    result = generate_subsets(nums)
    print(f"List: {nums}")
    print(f"Subsets ({len(result)}):")
    for subset in result:
        print(f"  {subset}")
    print()

# 5 examples with different lists
print_example([1, 2, 3])
print_example(['a', 'b'])
print_example([10, 20, 30, 40])
print_example([])
print_example([5])
