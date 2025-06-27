class Person:
    # Class variable - shared by all instances of Person
    # This list defines the different types of persons in the system
    types = ['Student','Teacher','Principal']
    
    def __init__(self,name = 'Unknown'):
        # Instance variable - unique to each Person object
        # Store the name of the person
        self.name = name
        # Print confirmation message when a Person object is created
        print("Person is creating...")
    
    def print_Name(self):
        # Instance method - can be called on any Person object
        # Prints the name of the specific person instance
        print("Name : ",self.name)
    
    @classmethod
    def get_types(cls):
        # Class method - belongs to the class, not to any specific instance
        # Can be called on the class itself or any instance
        # Returns the class variable 'types' 
        # 'cls' refers to the class (Person in this case)
        return cls.types
    
    @staticmethod
    def get_person():
            return Person()

# Create an instance of Person class with name 'Kulitha'
# This will call __init__ method and print "Person is creating..."
kulitha = Person('Kulitha')

# Call instance method on the kulitha object
# This will print "Name : Kulitha"
kulitha.print_Name()

# Access class variable directly through the class name
# This prints the list of person types: ['Student', 'Teacher', 'Principal']
print(Person.types)

# Call class method through the class name
# This also returns and prints the list: ['Student', 'Teacher', 'Principal']
# Alternative ways to call: kulitha.get_types() or Person.get_types()
print(Person.get_types())

p = Person.get_person()
print(p.name)