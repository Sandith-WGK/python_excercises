file_name = 'data.txt'
a = 5
b = 0
try:
    with open(file_name) as file:
        print(file.readlines())

    c = a/b
    print(c)    

except FileNotFoundError as e :
    print(f'No such file or directory {file_name}',e)    
except ZeroDivisionError as e:
    print('Can not division by zero. ',e)
except Exception as e:
    print('Something went wrong', e)
finally:
    print("Process completed.")        
