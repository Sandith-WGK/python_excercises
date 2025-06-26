def get_odd_even(a):
    return 'Odd' if a%2 == 1 else 'Even'

a = [12,34,7,45,67,89,23,56,78,90]


b = []
c = []
d = [get_odd_even(i) for i in a]
e = [get_odd_even(value) for i,value in enumerate(a) if i % 2 == 0]

for i in a:
    b.append(i)

c = [i for i in a]  



print(a)
print(b)
print(c)
print(d)
print(e)