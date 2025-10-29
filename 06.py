s = set()
s.add(20)#
s.add(20.0)#
## python matches the value of integer, it does not compares the data types,
## if the value is same then it consider as a same number.....
s.add('20')
print(s)
print(len(s))