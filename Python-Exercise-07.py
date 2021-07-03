# Organizing a List

List = ["Jack" , "Daniel" ,"Emma" , "Alex" , "John" , "Jason"]
List.sort()
print(List) #sort in order
# output = ['Alex', 'Daniel', 'Emma', 'Jack', 'Jason', 'John']

List.sort(reverse=True)
print(List) # reversing in order
# output = ['John', 'Jason', 'Jack', 'Emma', 'Daniel', 'Alex']

print(sorted(List)) # print sorted list just for once
# output = ['Alex', 'Daniel', 'Emma', 'Jack', 'Jason', 'John']

List.reverse() # just reversing in order you have entered your items in list(Not alphabetically)
print(List)
# output = ['Jason', 'John', 'Alex', 'Emma', 'Daniel', 'Jack']

print(len(List)) # it says how many items there are in your list
# output = 6

#Be careful to print them singly