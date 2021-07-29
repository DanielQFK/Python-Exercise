# Dictionary2 exercise

#1
Dictionary = {
    'name':'max' ,
    'lastname':'johanson' ,
    'age': 32 ,
    'field':'math' ,
    'friend':'eva' ,
    'nationality':'USA'
    
}
Name = Dictionary['name']
Last_name = Dictionary['lastname']
Age = Dictionary['age']
Field = Dictionary['field']
Friend = Dictionary['friend']
Nationality = Dictionary['nationality']
print(f"Hi , I'm {Name} {Last_name} \n and I'm {Age} years old. \n I study {Field} . \n My friend's name is {Friend} \n and we are from {Nationality}")
"""output = 
Hi , I'm max johanson 
 and I'm 32 years old. 
 I study math . 
 My friend's name is eva 
 and we are from USA
"""
Students = {
    'name1':'Daniel' ,
    'name2':'Alex' ,
    'name3':'Emma' ,
    'name4':'Natalie' ,
    'name5':'laksjdnnxj'
}

#2
for student, name in Students.items():
    print(f"{student} is {name}")
"""output :
name1 is Daniel
name2 is Alex
name3 is Emma
name4 is Natalie
name5 is laksjdnnxj
"""     

#3
for title in Students.keys():
    print(title)
"""output:
name1
name2
name3
name4
name5
"""    
#4
number = 1
for name in Students.values():
    print(f"Student number {number} is {name}.")
    number = number+1
"""output:
Student number 1 is Daniel.
Student number 2 is Alex.
Student number 3 is Emma.
Student number 4 is Natalie.
Student number 5 is laksjdnnxj.
"""    
#5
number = 1
for name in sorted(Students.values()):
    print(f"Student number {number} is {name}.")
    number = number+1
"""output:
Student number 1 is Alex.
Student number 2 is Daniel.
Student number 3 is Emma.
Student number 4 is Natalie.
Student number 5 is laksjdnnxj.
"""    

#6 
Info = {
    'my name':'Daniel' ,
    'my cars':['BMW' , 'Chevrolet' , 'Benz' , 'Cadilac']
}
print(f"My name is {Info['my name']} and my cars are ")
for my_cars in Info['my cars']:
    print({my_cars})
"""output :
My name is Daniel and my cars are 
{'BMW'}
{'Chevrolet'}
{'Benz'}
{'Cadilac'}
"""    




