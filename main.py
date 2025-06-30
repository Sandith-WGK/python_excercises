from os import path 
import person

if path.exists('person.py'):
    print('oh')
print(person.get_name())

print(__name__)

print(dir(person))