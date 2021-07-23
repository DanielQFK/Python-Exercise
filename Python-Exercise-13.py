# while loop exercises...

# 1.
# traps in while(that goes or keeps on untill an uncountable number...)

# in the below program it's obvious , because while is always 1 or true or false... so it 
# keeps on...
# #1 = True        2 = False
while 1:
  print(".")

# In this program you can see that if a lower than 100 so continue till it gets bigger 
# than 100 but there is a trap , you write a is a-1 to make it so the number of a is one
# number ... 
a = 1
while a >100:
    print("hello")
    a = a-1

# 2.
guess = 10
number = int(input("Please guess my number > "))
while number!=guess:
    if number>guess:
        number = int(input("Enter a lower number > "))
    if number<guess:
        number = int(input("Enter a higher number > "))

print("Congratulation ...≧^◡^≦...")
