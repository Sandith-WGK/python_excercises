file = open('data.txt')

# Read the entire file
#data = file.read()

# Print the data read from the file
#print(data)

for i,lne in enumerate(file):
    print("Line--->",i+1,lne)

# Close the file
file.close()

'''

'r' = read only
'w' = write with truncate
'x' = open for exclusive creation
'a' = append
'b' = binary
't' = text mode
'+' = updating
'''
file = open('data.txt', 'w')

# Write data to the file

x = [str(i) for i in range(20)]  # x is a LIST of strings
# x = ['0', '1', '2', '3', '4', '5', ..., '19']

msg = ','.join(x)  # msg is a STRING
# msg = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19'

""" What .join() does:

Input: Takes a list/iterable of strings
Output: Returns a single string
Process: Combines all elements with the specified separator

Before .join():
x = ['0', '1', '2', '3', '4']  ← LIST of strings

After .join():
msg = '0,1,2,3,4'  ← Single STRING """


file.write(msg)

# Close the file
file.close()

# open a file self closing
with open('data.txt', 'r') as file:
    for i, lne in enumerate(file):
        print("Line--->", i + 1, lne.strip())  # .strip() removes trailing newline characters