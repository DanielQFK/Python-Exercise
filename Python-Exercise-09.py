# input-int

# 1.
name = input("What is your name? > ")
last_name = input("What is your lastname ? > ")
age = int(input("How old are you ? > "))

print(f"I'm {name.title()} {last_name.title()} , and I'm {age} years old...")

# output = 

# What is your name? > daniel
# What is your lastname ? > tajik
# How old are you ? > 17
# I'm Daniel Tajik , and I'm 17 years old...

name1 = input("Enter one of your fiend's name > ")
name2 = input("Enter one of your fiend's name > ")
name3 = input("Enter one of your fiend's name > ")
name4 = input("Enter one of your fiend's name > ")
name5 = input("Enter one of your fiend's name > ")
names = [name1.title() , name2.title() , name3.title() , name4.title() , name5.title()]
print("Here are your friends' name : " , names)

# output = 
# Enter one of your fiend's name > max
# Enter one of your fiend's name > alex
# Enter one of your fiend's name > daniel
# Enter one of your fiend's name > joe
# Enter one of your fiend's name > james
# Here are your friends' name :  ['Max', 'Alex', 'Daniel', 'Joe', 'James']


