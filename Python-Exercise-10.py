# if/elif/else exercise

Name = input("Enter your name > ") 
Last_name = input("Enter your lastname > ")
Age = int(input("Enter your age > "))
if Name == "Daniel":
    print("Oh , we have the same name ... ")
else:
    print("You have a nice name... ")

if Last_name == "Tajik":
    print("Oh we have the same lastname...")
else:
    print("You have a nice lastname too ... ")

if Age <= 7:
    print("Sorry , I thing you have a mistake , because a 7 year old girl/boy or less , can't read... ")
elif 7<Age<15:
    print("Oh , come on , are you joking... ")
elif 15<=Age<20:
    print("Well done , you are a teenager...")
elif 20<=Age<30:
    print("You are getting mature...")
elif 30<=Age<60:
    print("I think you are a rational person...")
else:
    print("You are an experienced person and we should learn how to live from you ... ")   

# e.g. 2
Nationality = input("Where are you from? ")
if Nationality=="Iran" or Nationality=="iran" or Nationality=="IRN" or Nationality=="Islamic Republic of Iran":
    print("Hello Iranian... ")
elif Nationality=="U.S.A" or Nationality=="USA" or Nationality=="America" or Nationality=="United States of America":
    print("Hi American...")
#As you see we can also use or if we have many things to put in the condition...                   
