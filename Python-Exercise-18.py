# set exercise 2

Numbers = {1, 2, 3, 4, 5, 6, 7, 8, 10}
Numbers.add(9)
print(sorted(Numbers))
"""Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
Numbers.remove(10)
print(Numbers)
"""Output:{1, 2, 3, 4, 5, 6, 7, 8, 9}"""

Numbers.discard(9)
print(Numbers)
"""output:{1, 2, 3, 4, 5, 6, 7, 8, 9}"""

Numbers.pop()
print(Numbers)
"""ouput:{2, 3, 4, 5, 6, 7, 8}"""

Numbers.clear()
print(Numbers)
"""output:set()"""

a = {10, 20, 30}
b = {40, 50, 60}
c = {70, 80, 90}
all_numbers = a.union(b, c)
print(sorted(all_numbers))
"""output:[10, 20, 30, 40, 50, 60, 70, 80, 90]"""

print(sorted(a | b | c))
"""output:[10, 20, 30, 40, 50, 60, 70, 80, 90]"""


I = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
II = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(I & II)
"""output:{2, 3, 4, 5, 6, 7, 8, 9, 10}"""
Intersection = I.intersection(II)
print(Intersection)
"""output:{2, 3, 4, 5, 6, 7, 8, 9, 10}"""


print(II-I , I-II)
"""Output:{11} {1}"""

difference = I.difference(II)
print(difference)
"""Output = {1}"""

difference2 = II.symmetric_difference(I)
print(difference2)
"""output:{1, 11}"""

comparison = difference >= difference2
comparison2 = difference <= difference2
print(comparison)
print(comparison2)
"""output:
False
True"""

print(len(II))
"""output:10"""

