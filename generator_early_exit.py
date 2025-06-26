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

print("=" * 50)
print("SCENARIO: We only need the first 3 odd numbers")
print("=" * 50)

print("\n--- Using Regular Function ---")
regular_result = get_odd_regular(1000)  # Computes ALL 500 odd numbers!
print("Taking only first 3:")
first_three_regular = regular_result[:3]
print(f"Result: {first_three_regular}")

print("\n--- Using Generator ---")
generator_result = get_odd_generator(1000)  # Doesn't compute anything yet!
print("Taking only first 3:")
first_three_generator = []
for i, odd_num in enumerate(generator_result):
    first_three_generator.append(odd_num)
    if i == 2:  # Stop after getting 3 numbers
        break
print(f"Result: {first_three_generator}")

print("\n" + "=" * 50)
print("PERFORMANCE COMPARISON")
print("=" * 50)
print("Regular function: Computed 500 numbers, used only 3 (497 wasted!)")
print("Generator: Computed only 3 numbers (0 wasted!)")

#https://claude.ai/share/b5059a79-1b4d-4107-92b1-38cd6818ac2c