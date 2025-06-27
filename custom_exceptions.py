"""
Exception Handling Demo with Static Methods and Custom Exceptions

This program demonstrates:
1. Static methods for object creation with validation
2. Generic exception handling
3. Custom exception classes with error codes
4. Specific exception handling with multiple exception types

Author: [Your Name]
Date: [Current Date]
"""

class Person:
    """
    Represents a person with name and age attributes.
    Uses static method for validated object creation.
    """
    
    def __init__(self, name, age):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.name = name
        self.age = age

    @staticmethod
    def get_person(name, age):
        """
        Static factory method to create a Person with validation.
        
        This method validates input parameters before creating a Person object.
        Uses generic Exception class for error handling.
        
        Args:
            name (str): The person's name (must not be empty)
            age (int): The person's age (must be 0-119)
        
        Returns:
            Person: A new Person object if validation passes
            
        Raises:
            Exception: If name is empty or age is invalid
        
        Validation Rules:
            - Name must not be empty/None/False
            - Age must be between 0 and 119 (inclusive)
        """
        # Validate name - check for empty, None, or falsy values
        if not name:
            raise Exception('Invalid Name')
            
        # Validate age - must be realistic human age range    
        if age < 0 or age >= 120:
            raise Exception('Invalid Age')

        # If validation passes, create and return new Person object
        return Person(name, age)

# Example 1: Generic Exception Handling
# Try to create a Person with invalid age (-9)
try:
    # This will fail validation and raise an Exception
    p = Person.get_person('Kulitha', -9)
    print(p)  # This won't execute due to exception
    print(p.name, str(p.age))  # This won't execute either

except Exception as e:
    # Catch any Exception and print the error message
    print("Error found ", e)

# Program continues executing after exception is handled
print("Hey")


# ===== CUSTOM EXCEPTION CLASSES =====

class InvalidNameException(Exception):
    """
    Custom exception for invalid name errors.
    
    Inherits from the built-in Exception class and adds an error code
    for programmatic error identification.
    """
    
    def __init__(self, error):
        """
        Initialize the custom exception.
        
        Args:
            error (str): The error message to display
        """
        # Call parent Exception class constructor with error message
        super(InvalidNameException, self).__init__(error)
        # Add custom error code for identification
        self.errorCode = 10


class InvalidAgeException(Exception):
    """
    Custom exception for invalid age errors.
    
    Inherits from the built-in Exception class and adds an error code
    for programmatic error identification.
    """
    
    def __init__(self, error):
        """
        Initialize the custom exception.
        
        Args:
            error (str): The error message to display
        """
        # Call parent Exception class constructor with error message
        super(InvalidAgeException, self).__init__(error)
        # Add custom error code for identification
        self.errorCode = 5


class Animal:
    """
    Represents an animal with name and age attributes.
    Uses static method for validated object creation with custom exceptions.
    """
    
    def __init__(self, name, age):
        """
        Initialize an Animal object.
        
        Args:
            name (str): The animal's name
            age (int): The animal's age
        """
        self.name = name
        self.age = age

    @staticmethod
    def get_animal(name, age):
        """
        Static factory method to create an Animal with validation.
        
        This method validates input parameters before creating an Animal object.
        Uses custom exception classes for specific error types.
        
        Args:
            name (str): The animal's name (must not be empty)
            age (int): The animal's age (must be 0-14)
        
        Returns:
            Animal: A new Animal object if validation passes
            
        Raises:
            InvalidNameException: If name is empty (errorCode: 10)
            InvalidAgeException: If age is invalid (errorCode: 5)
        
        Validation Rules:
            - Name must not be empty/None/False
            - Age must be between 0 and 14 (typical pet lifespan range)
        """
        # Validate name - raise custom exception if invalid
        if not name:
            raise InvalidNameException('Invalid Name')
            
        # Validate age - animals typically live 0-15 years    
        if age < 0 or age >= 15:
            raise InvalidAgeException('Invalid Age')

        # If validation passes, create and return new Animal object
        return Animal(name, age)

# Example 2: Custom Exception Handling
# Try to create an Animal with valid parameters
try:
    # This should succeed - valid name and age
    a = Animal.get_animal('Scooby', 8)
    print(a)  # This will print the object reference
    print(a.name, str(a.age))  # This will print "Scooby 8"

except (InvalidNameException, InvalidAgeException) as e:
    """
    Catch multiple specific exception types in one except block.
    Both custom exceptions have errorCode attribute for identification.
    """
    
    # Check error code to determine specific error type
    if(e.errorCode == 10):
        # InvalidNameException has errorCode 10
        print("Invalid Name")

    elif(e.errorCode == 5):
        # InvalidAgeException has errorCode 5
        print("Invalid Age")
    else:
        # Fallback for unexpected error codes (defensive programming)
        print("Somethng went wrong")      

# Program continues executing after exception handling
print("Hey")

"""
Key Concepts Demonstrated:

1. STATIC METHODS (@staticmethod):
   - Don't need class instance to call
   - Used as factory methods for validated object creation
   - Called on class: Person.get_person() or Animal.get_animal()

2. GENERIC EXCEPTION HANDLING:
   - Uses built-in Exception class
   - Simple but less specific error information

3. CUSTOM EXCEPTIONS:
   - Inherit from Exception class
   - Can add custom attributes (errorCode)
   - Provide more specific error handling

4. MULTIPLE EXCEPTION HANDLING:
   - except (Exception1, Exception2) as e: syntax
   - Allows different handling for different error types
   - Can use custom attributes for fine-grained control

5. EXCEPTION FLOW:
   - try: code that might fail
   - except: handle the failure
   - Program continues after except block

6. VALIDATION PATTERNS:
   - Check inputs before processing
   - Raise specific exceptions for different error types
   - Use factory methods to encapsulate validation logic
"""
           