def get_odd_regular(upper_limit):
    """Regular function - computes ALL odd numbers"""
    print(f"Regular: Computing ALL odd numbers up to {upper_limit}")
    odd = []
    
    for i in range(0, upper_limit):
        if i % 2 == 1:
            print(f"Regular: Computing {i}")
            odd.append(i)
    
    print(f"Regular: Finished! Created list with {len(odd)} numbers")
    return odd

def get_odd_generator(upper_limit):
    """Generator - computes odd numbers on-demand"""
    print(f"Generator: Ready to generate odd numbers up to {upper_limit}")
    
    for i in range(0, upper_limit):
        if i % 2 == 1:
            print(f"Generator: Computing {i}")
            yield i
    
    print("Generator: Finished!")


print("\n" + "=" * 50)
print("REAL-WORLD EXAMPLE: Finding first odd number > 100")
print("=" * 50)

def find_first_odd_above_100_regular():
    """Using regular function - wasteful!"""
    print("Regular: Getting ALL odd numbers up to 10000...")
    all_odds = get_odd_regular(10000)  # Computes 5000 numbers!
    
    for num in all_odds:
        if num > 100:
            print(f"Regular: Found first odd > 100: {num}")
            return num

def find_first_odd_above_100_generator():
    """Using generator - efficient!"""
    print("Generator: Searching for first odd > 100...")
    
    for num in get_odd_generator(10000):  # Only computes what we need!
        if num > 100:
            print(f"Generator: Found first odd > 100: {num}")
            return num

print("\n--- Regular Function Approach ---")
result1 = find_first_odd_above_100_regular()

print("\n--- Generator Approach ---")
result2 = find_first_odd_above_100_generator()

print(f"\nBoth found: {result1}")
print("But look at the difference in computation!")
