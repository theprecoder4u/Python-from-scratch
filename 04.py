##LISTS - lists are mutable

fruits = ["apple", "banana"]
print(fruits[0]) 
fruits.append("Grapes")
fruits.insert(2,"Orange")
#list.pop(3)
#list.reverse()
#list.sort()
print(fruits)
##TUPLE - tuples are immutable
a = (1, 2, 3, 4, 5,5,5,5)
b = (6, 7, 8, 9, 10)

concatenated = a + b
print(concatenated)

no_of_5 = a.count(5)
print(no_of_5)
n = a.count(50)
print(n)