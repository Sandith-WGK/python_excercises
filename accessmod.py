class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25
        self._city = 'Galle'

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def sleep(self):
        print("Sleeping ... ", self.name)


class Student(Person):
    def __init__(self, name):
        self.name = name
        super(Student,self).__init__(name)

    def print_city(self):
        print(self._city)
praneeth = Person("Praneeth")
praneeth.sleep()
praneeth.set_age(30)
praneeth.__age = 50
stu = Student('Raj')
stu.print_city()

print("Name is ", praneeth.name)
print("Age is ", praneeth.get_age())
print("Age is ", praneeth.__age)