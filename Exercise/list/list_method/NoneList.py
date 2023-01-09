list1 = [None] * 5 # [None, None, None, None, None,]
print(list1)

print(type(None))
if list1:
    print("true") #출력됨

list2 = list((1,2,3))
list2 = list({1,2,3})

tuple1 = 1,2
tuple2 = 1,2,
if tuple1 == tuple2:
    print("same tuple elements")
print(id(tuple1))
print(id(tuple2))
if tuple1 is tuple2:
    print("same tuple reference")
else:
    print("false")

list3 = [1,2,3]
list4 = [1,2,3]
print(id(list3))
print(id(list4))
if list3 is list4:
    print("same list reference")
else:
    print("false")

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
print(len(x))
#print(max(x))
x= [1,2,3]
print(max(x))