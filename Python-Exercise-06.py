# List 2
# Changing, Adding, and Removing Elements in List
#exercises

List = ["Ryan" , "Sara" , "Maria"]
List.append("Max")
print(List)
#output = ['Ryan', 'Sara', 'Maria', 'Max']

List[0] = "Mohammad"
print(List)
#output = ['Mohammad', 'Sara', 'Maria', 'Max']

List.insert(-1 , "Nina")
print(List)
#output = ['Mohammad', 'Sara', 'Maria', 'Nina', 'Max']

List.remove("Max")
print(List)
#output = ['Mohammad', 'Sara', 'Maria', 'Nina']

List.pop(-1)
print(List)
#output = ['Mohammad', 'Sara', 'Maria']

del List[0]
print(List)
#output = ['Sara', 'Maria']