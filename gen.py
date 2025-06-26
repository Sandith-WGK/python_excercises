def get_odd(upper_limit):
    odd = []

    for i in range(0,upper_limit):
        if i % 2 ==1:
            print(i)
            odd.append(i)
            print(odd)
    return odd

x = get_odd(10)
print(x)         

def get_odd_gen(upper_limit):
    """Generator function to yield odd numbers up to upper_limit."""

    for i in range(0,upper_limit):
        if i % 2 ==1:
            print("Odd",i)
            yield i
            

# When you call the generator, it doesn't run immediately
y = get_odd_gen(10)  # Creates a generator object, doesn't execute yet

# It only runs when you ask for values
for i in y:
    print("loop",i) # Now it starts executing, yielding one value at a time
print(y)   