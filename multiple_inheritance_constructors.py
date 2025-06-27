class Animal:
    def __init__(self):
        print("Animal constructor called")

    def talk(self):
        print("Animal is talking")    

class Mammal:
    def __init__(self):
        print("Mammal constructor called")

    def talk(self):
        print("Mammal is talking")  

class Dog(Animal, Mammal):
    def __init__(self, name='Unknown'):
        print("Dog constructor called")
        
        # Method 1: Using super() - follows MRO (Method Resolution Order)
        super().__init__()  # This calls Animal.__init__() first
        
        # Method 2: Call specific parent constructors explicitly
        # Animal.__init__(self)  # Explicitly call Animal constructor
        # Mammal.__init__(self)  # Explicitly call Mammal constructor
        
        self.name = name
        print(f"Dog {self.name} created")

    def set_name(self, name):
        self.name = name

    def bark(self, msg):
        message = f"Baw Baw {msg} by {self.name}"
        print(message)

print("=" * 50)
print("CURRENT BEHAVIOR (only calls Animal constructor)")
print("=" * 50)

dog1 = Dog('Buddy')
print(f"MRO (Method Resolution Order): {Dog.__mro__}")

print("\n" + "=" * 50)
print("SOLUTION 1: Call both constructors explicitly")
print("=" * 50)

class DogExplicit(Animal, Mammal):
    def __init__(self, name='Unknown'):
        print("DogExplicit constructor called")
        
        # Explicitly call both parent constructors
        Animal.__init__(self)
        Mammal.__init__(self)
        
        self.name = name
        print(f"Dog {self.name} created")

    def bark(self, msg):
        message = f"Baw Baw {msg} by {self.name}"
        print(message)

print("Creating DogExplicit:")
dog2 = DogExplicit('Charlie')

print("\n" + "=" * 50)
print("SOLUTION 2: Cooperative inheritance with super()")
print("=" * 50)

class AnimalCoop:
    def __init__(self, **kwargs):
        print("AnimalCoop constructor called")
        super().__init__(**kwargs)  # Pass along to next in MRO

class MammalCoop:
    def __init__(self, **kwargs):
        print("MammalCoop constructor called")
        super().__init__(**kwargs)  # Pass along to next in MRO

class DogCoop(AnimalCoop, MammalCoop):
    def __init__(self, name='Unknown', **kwargs):
        print("DogCoop constructor called")
        super().__init__(**kwargs)  # This will call both parents!
        self.name = name
        print(f"Dog {self.name} created")

    def bark(self, msg):
        message = f"Baw Baw {msg} by {self.name}"
        print(message)

print("Creating DogCoop (cooperative inheritance):")
dog3 = DogCoop('Max')
print(f"MRO: {DogCoop.__mro__}")

print("\n" + "=" * 50)
print("SOLUTION 3: Modified original with both calls")
print("=" * 50)

class DogBoth(Animal, Mammal):
    def __init__(self, name='Unknown'):
        print("DogBoth constructor called")
        
        # Call both parent constructors
        Animal.__init__(self)
        Mammal.__init__(self)
        
        self.name = name
        print(f"Dog {self.name} created")

    def set_name(self, name):
        self.name = name

    def bark(self, msg):
        message = f"Baw Baw {msg} by {self.name}"
        print(message)

print("Creating DogBoth:")
dog4 = DogBoth('Rocky')
dog4.bark('Hello')
dog4.talk()  # Which talk() method gets called?

print("\n" + "=" * 50)
print("UNDERSTANDING METHOD RESOLUTION ORDER (MRO)")
print("=" * 50)

print("For class Dog(Animal, Mammal):")
print(f"MRO: {Dog.__mro__}")
print("This means:")
print("1. Dog methods are checked first")
print("2. Then Animal methods (first parent)")
print("3. Then Mammal methods (second parent)")
print("4. Finally object methods")

print("\nWhich talk() method gets called?")
dog4.talk()
print("↳ Animal's talk() because Animal comes first in MRO")

print("\n" + "=" * 50)
print("CALLING SPECIFIC PARENT METHODS")
print("=" * 50)

class DogSpecific(Animal, Mammal):
    def __init__(self, name='Unknown'):
        # Call both constructors explicitly
        Animal.__init__(self)
        Mammal.__init__(self)
        self.name = name

    def talk_like_animal(self):
        """Call Animal's talk method specifically"""
        Animal.talk(self)
    
    def talk_like_mammal(self):
        """Call Mammal's talk method specifically"""
        Mammal.talk(self)
    
    def talk(self):
        """Override to call both"""
        print(f"{self.name} can talk in multiple ways:")
        Animal.talk(self)
        Mammal.talk(self)

print("Creating DogSpecific with specific method calls:")
dog5 = DogSpecific('Bella')
print("\nCalling different talk methods:")
dog5.talk_like_animal()
dog5.talk_like_mammal()
dog5.talk()

print("\n" + "=" * 50)
print("BEST PRACTICES SUMMARY")
print("=" * 50)

print("""
1. EXPLICIT CALLS (Recommended for multiple inheritance):
   Animal.__init__(self)
   Mammal.__init__(self)

2. SUPER() WITH SINGLE INHERITANCE:
   super().__init__()  # Clean and follows MRO

3. COOPERATIVE INHERITANCE:
   Use **kwargs and super() in all classes
   Good for complex inheritance hierarchies

4. SPECIFIC METHOD CALLS:
   Animal.method_name(self)  # Call specific parent method
   
Choose based on your needs:
- Simple multiple inheritance → Explicit calls
- Complex hierarchies → Cooperative inheritance
- Need specific parent behavior → Explicit method calls
""")
