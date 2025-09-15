# myList = []
# lista = []
# list2 = []
# myList = ["Reymundo", "Lachica", "Fiesta", "Repollo"]
# lista =["Adarme", "Paltep"]
# list2 = ["Monje", "Espiritu"]
# print (myList)

# myList[2]
# print(myList[::-1])
# print(myList [1:4:2])
# print(myList [1:3:2])
# myList.append("Flores")
# myList.append(lista)
# myList.insert(1, "John")
# print("\t")
# print (myList)

# myList.pop()
# myList.pop(0)

# myList.remove("Lachica")

# print(myList + list2)
# print(myList.sort())
# myList.reverse()
# print(myList)

# print (myList)
# for x in myList:
#     print (f"{x}", end=" ")
# print("\t")

# for y in range(len(myList)):
#     print(f"{myList[y]}", end=" ")

# print("\t")

# mylist2 = []

# for x in range(3):
#     print ("Enter a number: ")
#     num1 = float (input())
#     mylist2.append(num1)
# print(mylist2)

# nestedList = [[12,5,3], [6,9,5]]
# nestedList[1] [0]
# nestedList[0] [1]

# for x in range (len(nestedList)):
#     for y in range (len(nestedList [x])):
#         print (f" {nestedList [x] [y]}", end=" ")
#     print()


# for x in range nestedList:
#     for y in x:
#         print(f"{y}", end = " ")
#         sum += y
#     print()
# mylist = []
# mylisted = []
# sum = 0
# ave = 0

# for x in range(2):
#     listed = []
#     print (f"row {x+1}")
#     for y in range(2):
#         print(f"row score {y+1}")
#         num = int (input())
#         listed.append(num)
#     mylisted.append(list)

# for x in mylist:
#     for y in x:
#         sum += y
#         ave = sum / len(mylisted)



myTuple = (1,4,5,6)
x = list (myTuple)
x.append(8)
x.append(70)
x.remove(5)
x.pop()

myTuple2  = (tuple (x))
print (myTuple2)

for x in myTuple2:
    print(x, end = " ")

mydict = {"id": "URDA-011",   "name": "Velasco", "salary": 10000.00}
mydict["age"] = 28
mydict["sex"] = "Male"
mydict["name"] = "Tugare"
mydict.popitem()
mydict.pop("name")
print(mydict)

print ("\t")

for x in mydict.keys():
    print(x)

for y in mydict.values():
    print(y)

for x,y in mydict.items():
    print(f"Key: {x}, Value: {y}", end = " ")

