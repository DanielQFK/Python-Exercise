# set Exercise
# Part 1...

Integer_set = {1.2 , 19827 , 52435 , 234 , 21 , 47756.0938774}
print(Integer_set)
""""
output: {1.2, 234, 47756.0938774, 19827, 52435, 21}
"""

# Tip:set doesn't accept .title or .upper and ...
String_set = {"Kim" , "Tom" , "luara" , "John" , "BOB"}
# print(String_set.title())
"""
output:Traceback (most recent call last):
  File "Python-Exercise-17.py", line 11, in <module>
    print(String_set.title())
AttributeError: 'set' object has no attribute 'title'
"""

Mix_set = {"Ariana" , "weeky" , 32}
# print(f"His name is {Mix_set[0]} and his lastname is {Mix_set[1]} and he is {Mix_set[2]} years old...")
"""output:
Traceback (most recent call last):
  File "Python-Exercise-17.py", line 21, in <module>
    print(f"His name is {Mix_set[0]} and his lastname is {Mix_set[1]} and he is {Mix_set[2]} years old...")
TypeError: 'set' object is not subscriptable
"""

List_set = set(["it's a list" , 1 , "in a " , 2 , "set ."])
print(List_set)
"""
output: {"it's a list", 2, 1, 'in a ', 'set .'}
"""

duplicated_set = set([1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1])
print(duplicated_set)
"""
output:{1}
"""
loop_set = {"Liam" , "Scarlet" , "Emma" , "Ella" , "Nick"}
n = 1
for x in loop_set:
    print(x , "is my classmate number" , n , ".")
    n = n+1
# n = number
"""output:
Ella is my classmate number 1 .
Scarlet is my classmate number 2 .
Emma is my classmate number 3 .
Liam is my classmate number 4 .
Nick is my classmate number 5 .
"""
Check_set = {"Kim" , "Tom" , "luara" , "Liam" , "Scarlet" , "Emma" , "Ella" , "Nick" , "John" , "BOB" , "Ariana" , "weeky"}
print("Ella" in Check_set)
print("BOB" in Check_set)
print("Patrick" in Check_set)
"""
Output:
True
True
False
"""
