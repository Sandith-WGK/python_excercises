class Animal:

    def __init__(self):
        print("Anmal")

    def talk(self):
        print("Animal is talking")    

class Mammal:

    def __init__(self):
        print("Mammel")

    def talk(self):
        print("Animal is talking")  

class Dog(Animal,Mammal):
    #name = 'Unknown'
    #breed = ''

    def __init__(self,name= 'Unknown'):
        super(Dog,self).__init__()
        self.name = name
        

    def set_name(self,name):
        self.name = name

    def bark(self,msg):
        message = f"Baw Baw {msg} by {self.name}"
        print(message)

dog1 = Dog()
dog1.set_name('Chubby')
dog1.bark('Hello')

dog2 = Dog('Revon')
dog2.bark('Hi')
dog2.talk()
print(dog2.name)

