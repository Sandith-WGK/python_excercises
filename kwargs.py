def my_form(**params):

    if 'name' not in params:
        print("Name is required.")
    else:
        for key,value in params.items():
            if key == 'name':
                print("Name:", value)
            elif key == 'age':
                print("Age:", value)
            elif key == 'city':
                print("City:", value)
            elif key == 'country':
                print("Country:", value)
            else:
                print(f"Unknown parameter: {key} with value {value}")    


def hex_form(*values, ** params):
    print(values)
    if 'name' not in params:
        print("Error")
    else:
        print("Hello", params['name'])

hex_form(1, 78, height=176, city="Panadura")
hex_form(name="Praneeth", height=176)









my_form(name="John",age=30,city="New York",country="USA")
my_form(name="Alice",age=25,city="Los Angeles")