# ENUMERATE() - Works with ANY iterable (list, tuple, string, etc.)
# Purpose: Adds index numbers to any sequence

print("=" * 50)
print("ENUMERATE() - Adds index to any iterable")
print("=" * 50)

# With lists
fruits = ['apple', 'banana', 'orange']
print("enumerate() with list:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\n" + "-" * 30)

# With strings
word = "hello"
print("enumerate() with string:")
for index, char in enumerate(word):
    print(f"Index {index}: {char}")

print("\n" + "-" * 30)

# With custom start value
print("enumerate() with custom start:")
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")

print("\n" + "=" * 50)
print("DICTIONARY .items() - Only works with dictionaries")
print("=" * 50)

# Dictionary .items()
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print("dictionary.items():")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

print("\n" + "=" * 50)
print("KEY DIFFERENCES")
print("=" * 50)

print("\n1. WHAT THEY RETURN:")
print("-" * 25)
print("enumerate() returns: (index, value)")
print("dict.items() returns: (key, value)")

print("\n2. WHAT THEY WORK WITH:")
print("-" * 25)
print("enumerate(): ANY iterable (list, tuple, string, etc.)")
print("dict.items(): ONLY dictionaries")

print("\n3. PRACTICAL EXAMPLES:")
print("-" * 25)

# Example 1: Processing a list with position info
print("\nExample 1 - Processing list items with their positions:")
scores = [85, 92, 78, 96]
for position, score in enumerate(scores, 1):
    print(f"Student {position}: {score}%")

# Example 2: Processing dictionary key-value pairs
print("\nExample 2 - Processing dictionary data:")
grades = {'math': 85, 'science': 92, 'english': 78}
for subject, grade in grades.items():
    print(f"{subject.title()}: {grade}%")

print("\n" + "=" * 50)
print("COMMON CONFUSION: Using enumerate() on dictionaries")
print("=" * 50)

# What happens when you use enumerate on a dictionary?
print("enumerate() on dictionary (confusing!):")
for index, key in enumerate(person):
    print(f"Index {index}: Key '{key}' (value not directly accessible)")

print("\nBetter approach - use .items():")
for key, value in person.items():
    print(f"Key '{key}': Value '{value}'")

print("\nOr combine both if you need index AND key-value pairs:")
for index, (key, value) in enumerate(person.items()):
    print(f"Index {index}: {key} = {value}")

print("\n" + "=" * 50)
print("WHEN TO USE WHICH?")
print("=" * 50)

print("""
Use enumerate() when:
- You need the position/index of items
- Working with lists, tuples, strings
- You want to number items (like creating a menu)

Use .items() when:
- You have a dictionary
- You need both keys and values
- You're processing key-value pairs

Examples:
- enumerate(): "Show me item #1, item #2, etc."
- .items(): "Show me all key-value pairs"
""")

print("\n" + "=" * 50)
print("REAL-WORLD USAGE EXAMPLES")
print("=" * 50)

# Real example 1: Creating a numbered menu
print("Creating a numbered menu with enumerate():")
menu_items = ['Pizza', 'Burger', 'Salad', 'Pasta']
for num, item in enumerate(menu_items, 1):
    print(f"{num}. {item}")

print("\nProcessing user settings with .items():")
settings = {'theme': 'dark', 'notifications': True, 'language': 'en'}
for setting, value in settings.items():
    print(f"Setting '{setting}' is set to: {value}")
