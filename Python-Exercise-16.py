# Fnction exercises

# e.g. 1
def Function1():
    print("Hi")

Function1()

# e.g. 2
def Function2():
    a = 3
    b = 3
    c = a+b
    d = a*b
    print(c , d)

Function2()

# e.g. 3
def Function3(name , lastname):
    print(f'my name is {name} and my lastname is {lastname}...')

Function3('Joe' , 'Stone')

# e.g. 4
def Function4(a , b):
    minus = b-a
    return minus

result = Function4(2 , 8)
print(result)    

"""
outputs in order:
Hi
6 9
my name is Joe and my lastname is Stone...
6
"""
