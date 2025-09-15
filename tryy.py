# num1 = int (input("Enter matix size: "))

# for x in range (1, num1 + 1): 
#     for y in range (1,num1 + 1) :
#       if x%2 == 0:
#         print(f"*", end = " ")
#       else:
#          print ("o", end = " ")
#     print ()


# while (True):


#     str = input (print("Enter tring: "))
#     if (str == "/"):
#         break;
#     for z in str:
#      print(z)



#     for a in range (len(str)):
#         match(str[a]):
#             case "a":
#                 print (f"{str[a]} vowel" )
#             case "e":
#                 print (f"{str[a]} vowel" )
#             case "i":
#                 print (f"{str[a]} vowel" )
#             case "o":
#                 print (f"{str[a]} vowel" )
#             case "u":
#                 print (f"{str[a]} vowel" )
#             case _ :
#                 print(f"{str[a]} consonant")


# num = int (input("Enter a number: "))

# divisor = []
# for x in  range (1, num + 1):
#     if num % x == 0:
#         divisor.append(x)
# print (f"{num} is divisible by {divisor}")

# if num % 5 == 0:
#     print (f"{num} is divisible by 5")

# if num % 6 == 0:
#     print (f"{num} is divisible by 6")


# while (True):

#     str = input ("Enter a string: ")
#     if (str == "/"):
#         break;
    
while (True):    

    num = int (input("Enter a number: "))

    if num % 5 == 0:
        print (f"{num} is divisible by 5")
    if num % 6 == 0:
        print (f"{num} is divisible by 6")

    divior = []
    for x in range (1, num + 1):
        if num % x == 0:
            divior.append(x)
    print(divior)
